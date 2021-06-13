//Programmer: Chris Tralie
//Purpose: To provide an engine for the wheel of fortune app
var namestxt;
HarryPotterNames = ['Hannah Abbot', 'Susan Bones', 'Cho Chang', 'Michael Corner', 'Colin Creevey', 'Seamus Finnigan', 'Marcus Flint', 'Gregory Goyle', 'Anthony Goldstein', 'Hermione Granger', 'Angelina Johnson', 'Lee Jordan', 'Neville Longbottom', 'Luna Lovegood', 'Draco Malfoy', 'Pansy Parkinson', 'Padma Patil', 'Parvati Patil', 'Harry Potter', 'Zacharius Smith', 'Romilda Vane', 'Fred Weasley', 'George Weasley', 'Ginny Weasley', 'Ron Weasley', 'Oliver Wood', 'Blaise Zabini']; //Harry Potter student names

var perm = [13, 22,  4,  7, 17, 23,  0, 16, 21,  9,  6, 25, 12,  1,  2, 24, 14, 26, 19, 10, 15, 20,  3, 11,  5, 18,  8]; //Random permutation fixed ahead of time

var names = HarryPotterNames;
var angle = 0;
var finalAngle = 0;
var spinning = false;
var targetTime = 0;
var startTime = Date.now();
var omega0 = 0; //Initial angular velocity
var alpha = 0.2; //Negative angular acceleration
var angle0 = 0;

function drawWheel() {
    var colors = ['#FFAAAA', '#AAFFAA', '#AAAAFF', '#FFFF00', '#00FFFF', '#FF00FF'];
    var N = names.length;
    var theta = 2*Math.PI/N;    
    var canvas = document.getElementById("wof");
    var ctx = canvas.getContext("2d");
    var W = canvas.width;
    var H = canvas.height;
    var nextX = W/2*Math.cos(theta);
    var nextY = W/2*Math.sin(theta);
    
    ctx.font = "30px Arial";
    ctx.translate(W/2, H/2);
    ctx.rotate(angle);
    
    for (var i = 0; i < N; i++) {
        ctx.rotate(2*Math.PI*i/N);
        ctx.fillStyle = colors[i%colors.length];
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(W/2, 0);
        ctx.lineTo(nextX, nextY);
        ctx.closePath();
        ctx.fill();    
        ctx.rotate(-2*Math.PI*i/N);
    }
    ctx.fillStyle = "#000000";
    for (var i = 0; i < N; i++) {
        ctx.rotate(2*Math.PI*(i- 0.25)/N);
        ctx.fillText(names[i],W/6, 0);
        ctx.rotate(-2*Math.PI*(i - 0.25)/N);
    }
    ctx.rotate(-angle); //Undo global rotation
    
    ctx.beginPath();
    ctx.moveTo(W/2.5, 0);
    ctx.lineTo(W/2, 0);
    ctx.lineTo(W/2, H/20);
    ctx.fill();
    
    ctx.translate(-W/2, -H/2);
    if (spinning) {
        var t = (Date.now() - startTime) / 1000.0;
        angle = angle0 + omega0*t - 0.5*alpha*t*t;
        if (targetTime - t < 0) {
            console.log("targetTime = " + targetTime + ", stopping t = " + t + ", angle = " + angle + ", finalAngle = " + finalAngle);
            spinning = false;
        }
        requestAnimationFrame(drawWheel);
    }
}
