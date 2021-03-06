function getMousePos(canvas, evt) {
	var rect = canvas.getBoundingClientRect();
	return {
	    X: evt.clientX - rect.left,
	    Y: evt.clientY - rect.top
	};
}

var TOLCLOSE = 2;
var TOLSNAP = 20;  //If the user is within this many pixels of one of the bisectors, snap them to the nearest point
var DEFLINEWIDTH = 1; //Default line width
var SELLINEWIDTH = 5; //Selected line width
var canvas = document.getElementById('segcanvas');
var ctx = canvas.getContext("2d"); //For drawing
//Need this to disable that annoying menu that pops up on right click
canvas.addEventListener("contextmenu", function(e){ e.stopPropagation(); e.preventDefault(); return false; }); 

colors = ["#ff0000", "#00ff00", "#0000ff"];
colors2 = ["#ff00ff", "#ffff00", "#00ffff"];

var Ps = []; //Points on the triangle
var Qs = []; //Edge midpoints
var Vs = []; //Perpendicular bisector directions
var currPoint = vec3.create(); //Current point snapped from closest dragged mouse point
var currR = 0.0; //Current radius
var currBisector = -1; //Index of the side whose bisector is closest to the mouse
var allClose = false; //Whether or not the current point is close to equidistant to all three

//Temporary variables
var P1 = vec3.create();
var P2 = vec3.create();

function repaint() {
    var dW = 5;
    var dWSel = 10;
    var W = canvas.width;
    var H = canvas.height;
    ctx.clearRect(0, 0, W, H);
    ctx.lineWidth = DEFLINEWIDTH;
    
    //Draw triangle points
    for (var i = 0; i < Ps.length; i++) {
        ctx.fillStyle = colors[i];
        ctx.fillRect(Ps[i][0]-dW, Ps[i][1]-dW, dW*2+1, dW*2+1);
    }
    
    //Draw triangle edges
    for (var i = 0; i < Ps.length; i++) {
        ctx.fillStyle = colors2[i];
        ctx.beginPath();
        ctx.moveTo(Ps[i][0], Ps[i][1]);
        ctx.lineTo(Ps[(i+1)%Ps.length][0], Ps[(i+1)%Ps.length][1]);
        ctx.stroke();        
    }
    
    //Draw bisectors
    ctx.fillStyle = "#444444";
    if (Ps.length == 3) {
        for (var i = 0; i < 3; i++) {
            ctx.fillStyle = colors2[i];
            if (i == currBisector) {
                ctx.lineWidth = SELLINEWIDTH;
            }
            else {
                ctx.lineWidth = DEFLINEWIDTH;
            }
            //Draw the lines long enough so that they'll fill the entire canvas
            vec3.scaleAndAdd(P1, Qs[i], Vs[i], -1000);
            vec3.scaleAndAdd(P2, Qs[i], Vs[i], 1000);
            ctx.beginPath();
            ctx.moveTo(P1[0], P1[1]);
            ctx.lineTo(P2[0], P2[1]);
            ctx.stroke();              
        }
    }
    ctx.lineWidth = DEFLINEWIDTH;
    
    //Draw equidistant points
    ctx.fillStyle = "#000000";
    if (allClose) {
        for (var i = 0; i < Ps.length; i++) {
            ctx.fillRect(Ps[i][0]-dWSel, Ps[i][1]-dWSel, dWSel*2+1, dWSel*2+1);
        }        
    }
    else if (currBisector > -1){
        ctx.fillRect(Ps[currBisector][0]-dWSel, Ps[currBisector][1]-dWSel, dWSel*2+1, dWSel*2+1);
        ctx.fillRect(Ps[(currBisector+1)%3][0]-dWSel, Ps[(currBisector+1)%3][1]-dWSel, dWSel*2+1, dWSel*2+1);
    }
    
    //Draw circle
    if (currR > 0) {
        if (allClose) {
            ctx.lineWidth = SELLINEWIDTH;
        }
        else {
            ctx.lineWidth = DEFLINEWIDTH;
        }
        ctx.beginPath();
        ctx.arc(currPoint[0], currPoint[1], currR, 0, 2*Math.PI);
        ctx.stroke();
    }
}

function selectPoint(evt) {
    if (!choosePoints) {
        return;
    }
    var mousePos = getMousePos(canvas, evt);
    var X = mousePos.X;
    var Y = mousePos.Y;
    var clickType = "LEFT";
    evt.preventDefault();
    if (evt.which) {
        if (evt.which == 3) clickType = "RIGHT";
        if (evt.which == 2) clickType = "MIDDLE";
    }
    else if (evt.button) {
        if (evt.button == 2) clickType = "RIGHT";
        if (evt.button == 4) clickType = "MIDDLE";
    }
    
    if (clickType == "LEFT") {
        //Add a point
        if (Ps.length < 3) {
            Ps.push(vec3.fromValues(X, Y, 0));
        }
        else {
            //If there's already a third point, simply replace it
            Ps[2] = vec3.fromValues(X, Y, 0);
        }
    }
    else {
        //Remove point
        if (Ps.length > 0) {
            Ps.pop();
        }
    }
    //Update perpendicular bisectors
    if (Ps.length == 3) {
        var N = vec3.fromValues(0, 0, 1);
        for (var i = 0; i < Ps.length; i++) {
            var dP1P2 = vec3.clone(Ps[(i+1)%Ps.length]);
            vec3.subtract(dP1P2, dP1P2, Ps[i]);
            Qs[i] = vec3.create();
            vec3.scaleAndAdd(Qs[i], Ps[i], dP1P2, 0.5);
            Vs[i] = vec3.create();
            vec3.cross(Vs[i], dP1P2, N);
            vec3.normalize(Vs[i], Vs[i]);
        }
    }
    repaint();
}

//Vectors to help determine distances to perpendicular bisectors
var dV = vec3.create();
var VProj = vec3.create();

function movePoint(evt) {
    if (choosePoints) {
        return; //Not dragging, still choosing triangle points
    }
    if (Ps.length < 3) {
        return; //Not enough points yet to make a triangle
    }
    var mousePos = getMousePos(canvas, evt);
    var X = mousePos.X;
    var Y = mousePos.Y;
    
    var V = vec3.fromValues(X, Y, 0);
    var ds = [0, 0, 0];
    var numClose = 0;
    currR = 0.0;
    //Compute perpendicular distance to all three bisectors Qs[i] + tVs[i]
    for (var i = 0; i < 3; i++) {
        vec3.subtract(dV, V, Qs[i]);
        var proj = vec3.dot(dV, Vs[i]);
        vec3.scaleAndAdd(VProj, Qs[i], Vs[i], proj);
        ds[i] = vec3.squaredDistance(VProj, V);
        if (ds[i] < TOLSNAP*TOLSNAP) {
            //Snap to the perpendicular bisector
            currPoint = vec3.clone(VProj);
            currR = vec3.distance(currPoint, Ps[i]);
            currBisector = i;
        }
    }
    //If the mouse point is close enough to all three, then it's close enough
    //to the circumcenter so highlight all three points
    allClose = true;
    for (var i = 0; i < 3; i++) {
        if (ds[i] > TOLCLOSE*TOLCLOSE) {
            allClose = false;
            break;
        }
    }
    
    repaint();
}

function choosePoints() {
    choosePoints = true;
}

function dragMouse() {
    choosePoints = false;
}

canvas.addEventListener("mousedown", selectPoint);
canvas.addEventListener("touchstart", selectPoint);
canvas.addEventListener("mousemove", movePoint);
repaint();
