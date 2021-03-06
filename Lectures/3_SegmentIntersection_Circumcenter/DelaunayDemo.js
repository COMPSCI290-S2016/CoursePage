var choosingPointsD = true;
var displayCircles = false;
var displayCenters = false;
var delcanvas = document.getElementById('delcanvas');
var delctx = delcanvas.getContext("2d"); //For drawing
//Need this to disable that annoying menu that pops up on right click
delcanvas.addEventListener("contextmenu", function(e){ e.stopPropagation(); e.preventDefault(); return false; }); 

colors = ["#ff0000", "#00ff00", "#0000ff"];
colors2 = ["#ff00ff", "#ffff00", "#00ffff"];

var PsD = []; //Points on the triangle
var Ts = []; //Delaunay triangles (flattened indices into the PsD array)
var Cs = []; //Triangle circumcenters
var Rs = []; //Circumcircle radii

function delRepaint() {
    var dW = 5;
    var dWSel = 10;
    var W = delcanvas.width;
    var H = delcanvas.height;
    delctx.clearRect(0, 0, W, H);
    
    //Draw points
    delctx.fillStyle = "#000000";
    for (var i = 0; i < PsD.length; i++) {
        delctx.fillRect(PsD[i][0]-dW, PsD[i][1]-dW, dW*2+1, dW*2+1);
    }
    
    //Draw DT edges
    delctx.lineWidth = 2;
    var i1, i2;
    for (var i = 0; i < Ts.length/3; i++) {
        for (var k = 0; k < 3; k++) {
            i1 = Ts[i*3+k];
            i2 = Ts[i*3+(k+1)%3];
            delctx.beginPath();
            delctx.moveTo(PsD[i1][0], PsD[i1][1]);
            delctx.lineTo(PsD[i2][0], PsD[i2][1]);
            delctx.stroke();        
        }
    }
    
    if (displayCenters) {
        delctx.fillStyle = "#FF0000";
        for (var i = 0; i < Cs.length; i++) {
            delctx.fillRect(Cs[i][0]-dW, Cs[i][1]-dW, dW*2+1, dW*2+1);
        }
    }
    
    if (displayCircles) {
        for (var i = 0; i < Cs.length; i++) {
            delctx.beginPath();
            delctx.arc(Cs[i][0], Cs[i][1], Rs[i], 0, 2*Math.PI);
            delctx.stroke();
        }
    }
}

function delSelectPoint(evt) {
    if (!choosingPointsD) {
        return;
    }
    var mousePos = getMousePos(delcanvas, evt);
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
        PsD.push([X, Y]);
    }
    else {
        //Remove point
        if (PsD.length > 0) {
            PsD.pop();
        }
    }
    delRepaint();
}

function calculateCircumcenters() {
    var NTris = Ts.length/3;
    Cs = new Array(NTris);
    Rs = new Array(NTris);
    var res;
    var vs = [null, null, null];
    for (var i = 0; i < NTris; i++) {
        for (var k = 0; k < 3; k++) {
            vs[k] = vec3.fromValues(PsD[Ts[i*3+k]][0], PsD[Ts[i*3+k]][1], 0);
        }
        res = getTriangleCircumcenter(vs[0], vs[1], vs[2]);
        Cs[i] = res.Circumcenter;
        Rs[i] = res.Radius;
    }
}

function choosePointsD() {
    choosingPointsD = true;
    delRepaint();
}

function doDelaunay() {
    choosingPointsD = false;
    Ts = Delaunay.triangulate(PsD);
    calculateCircumcenters();
    delRepaint();
}

delcanvas.addEventListener("mousedown", delSelectPoint);
delcanvas.addEventListener("touchstart", delSelectPoint);
delRepaint();

var displayCirclesCheckbox = document.getElementById('displayCirclesCheckbox');
displayCirclesCheckbox.addEventListener('change', function(e) {
    displayCircles = displayCirclesCheckbox.checked;
    delRepaint();
});
displayCirclesCheckbox.checked = false;

var displayCentersCheckbox = document.getElementById('displayCentersCheckbox');
displayCentersCheckbox.addEventListener('change', function(e) {
    displayCenters = displayCentersCheckbox.checked;
    delRepaint();
});
displayCentersCheckbox.checked = false;
