function getTriangleCircumcenter(a, b, c) {
    //Compute triangle normal
    var ab = vec3.create();
    vec3.subtract(ab, b, a);
    var ac = vec3.create();
    vec3.subtract(ac, c, a);
    var N = vec3.create();
    vec3.cross(N, ab, ac);
    vec3.normalize(N, N);
    
    //First perpendicular bisector
    var P = vec3.create();
    vec3.scaleAndAdd(P, a, ab, 0.5);
    var VP = vec3.create();
    vec3.cross(VP, N, ab);
    vec3.normalize(VP, VP);
    
    //Second perpendicular bisector
    var Q = vec3.create();
    vec3.scaleAndAdd(Q, a, ac, 0.5);
    var VQ = vec3.create();
    vec3.cross(VQ, N, ac);
    vec3.normalize(VQ, VQ);

    //Use cramer's rule and linear dependece of 3 equations
    //[A B][t] = [E]
    //[C D][s] = [F] 
    var A = VP[0] + VP[2];
    var B = -(VQ[0] + VQ[2]);
    var E = (Q[0]-P[0]) + (Q[2]-P[2]);
    var C = VP[1];
    var D = -VQ[1];
    var F = Q[1] - P[1];
    //console.log(A + " " + B + " " + E + "\n" + C + " " + D + " " + F);
    var detDenom = A*D - C*B;
    if (Math.abs(detDenom) < 1e-10) {
        console.log("detDenom too small: " + detDenom);
        return {Circumcenter:vec3.fromValues(0, 0, 0), Radius:0.0};
    }
    var detNumt = E*D - B*F;
    var detNums = A*F - C*E;
    var t = detNumt / detDenom;
    var s = detNums / detDenom;
    //console.log("s = " + s + ", t = " + t);
    var ret = vec3.create();
    vec3.scaleAndAdd(ret, P, VP, t);
    //Compute the radius from one of the points
    var R = vec3.distance(a, ret);
    return {Circumcenter:ret, Radius:R, P:P, Q:Q, VP:VP, VQ:VQ};
}


//This is code that Chris Tralie has written in to help plot the results
//for help debugging.  Feel free to browse the code to see how plot.ly works
//and ask any questions on the forum

//This is the way I hack the axes to be equal
function getAxesEqual(vs) {
    //Determine the axis ranges
    minval = 0;
    maxval = 0;
    for (var i = 0; i < vs.length; i++) {
        for (var j = 0; j < 3; j++) {
            if (vs[i][j] < minval){ minval = vs[i][j]; }
            if (vs[i][j] > maxval){ maxval = vs[i][j]; }
        }
    }
    return {
    x:{ x: [minval, maxval], y: [0, 0], z: [0, 0],
      mode: 'lines', line: {color: '#000000', width: 1}, type: 'scatter3d', name:'xaxis'
    },
    y:{ x: [0, 0], y: [minval, maxval], z: [0, 0],
      mode: 'lines', line: {color: '#000000', width: 1}, type: 'scatter3d', name:'yaxis'
    },
    z:{ x: [0, 0], y: [0, 0], z: [minval, maxval],
      mode: 'lines', line: {color: '#000000', width: 1}, type: 'scatter3d', name:'zaxis'
    }};
}

function getMousePos(canvas, evt) {
	var rect = canvas.getBoundingClientRect();
	return {
	    X: evt.clientX - rect.left,
	    Y: evt.clientY - rect.top
	};
}


