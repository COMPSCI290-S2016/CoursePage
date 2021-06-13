//Chris Tralie's solutions to Mini Assignment 1 Parts 1 and 2

//////////////////////////////////////////////
///********    Geometry Functions   *******///
//////////////////////////////////////////////
//Purpose: Project vector u onto vector v using the glMatrix library
//Inputs: u (vec3), v (vec3)
//Returns: projv (vec3), the projection of u onto v
function projVector(u, v) {
    var scale = (vec3.dot(u, v)/vec3.dot(v, v));//The scale in front of v is (u dot v) / (v dot v)
    var projv = vec3.create(); //Allocate a vector to hold the output
    vec3.scale(projv, v, scale); //Scale v by the appropriate amount
    return projv; //Return the result
}

//Purpose: To compute the perpendicular projection of a vector u onto a vector v
//Inputs: u (vec3), v (vec3)
//Returns: projperpv (vec3), the projection of u onto v
function projPerpVector(u, v) {
    var projv = projVector(u, v);
    var projperpv = vec3.create();
    vec3.subtract(projperpv, u, projv);
    return projperpv;
}


function getAngle(a, b, c) {
    var ab = vec3.create();
    vec3.subtract(ab, b, a);
    var ac = vec3.create();
    vec3.subtract(ac, c, a);
    var dot = vec3.dot(ab, ac);
    var angle = Math.acos(dot/Math.sqrt(vec3.dot(ab, ab)*vec3.dot(ac, ac)));
    console.log("angle = " + angle);
    return angle;
}

function getAboveOrBelow(a, b, c, d) {
    var ab = vec3.create();
    vec3.subtract(ab, b, a);
    var ac = vec3.create();
    vec3.subtract(ac, c, a);
    var ad = vec3.create();
    vec3.subtract(ad, d, a);
    var cross = vec3.create();
    vec3.cross(cross, ab, ac);
    var ret = vec3.dot(cross, ad);
    if (ret < 0) {
        ret = -1;
    }
    else if (ret > 0) {
        ret = 1;
    }
    return ret;
}

//Purpose: Given three 3D vertices a, b, and c, compute the area of the triangle
//spanned by them
//Inputs: a (vec3), b (vec3), c (vec3)
//Returns: area (float)
function getTriangleArea(a, b, c) {
    var ab = vec3.create();
    vec3.subtract(ab, b, a);
    var ac = vec3.create();
    vec3.subtract(ac, c, a);
    var cross = vec3.create();
    vec3.cross(cross, ab, ac);
    var area = 0.5*vec3.length(cross);
    return area;
}

function get3DLineIntersection(P, Vp, Q, Vq) {
    //Set up the system of 3 equations
    var A = [[Vp[0], -Vq[0]], [Vp[1], -Vq[1]], [Vp[2], -Vq[2]]];
    var b = [Q[0] - P[0], Q[1] - P[1], Q[2] - P[2]];
    //Make into a 2D system by multiplying both sides of the matrix equation 
    //on the left by A^T
    var ATA = [[0, 0], [0, 0]];
    var ATb = [0, 0];
    for (var i = 0; i < 2; i++) {
        for (var j = 0; j < 2; j++) {
            for (var k = 0; k < 3; k++) {
                ATA[i][j] += A[k][i]*A[k][j];
            }
        }
    }
    for (var i = 0; i < 2; i++) {
        for (var k = 0; k < 3; k++) {
            ATb[i] += A[k][i]*b[k];
        }
    }
    //Use 2D cramer's rule after 
    //[A B][t] = [E]
    //[C D][s] = [F] 
    //console.log(A + " " + B + " " + E + "\n" + C + " " + D + " " + F);
    //var A = ATA[0][0], B = ATA[0][1], E = ATb[0];
    //var C = ATA[1][0], D = ATA[1][1], F = ATb[1];
    var detDenom = ATA[0][0]*ATA[1][1] - ATA[1][0]*ATA[0][1];
    //Check for parallel lines
    if (Math.abs(detDenom) < 1e-10) {
        console.log("detDenom too small: " + detDenom);
        return null;
    }
    var detNumt = ATb[0]*ATA[1][1] - ATA[0][1]*ATb[1];
    var detNums = ATA[0][0]*ATb[1] - ATA[1][0]*ATb[0];
    var t = detNumt / detDenom;
    var s = detNums / detDenom;
    //console.log("s = " + s + ", t = " + t);
    var ret = vec3.create();
    vec3.scaleAndAdd(ret, P, Vp, t);
    return {P:ret, t:t, s:s};  //Return the point of intersect, as well as
    //the parameters s and t
}


//Purpose: Given a line segment ab and a line segment cd, compute the intersection
//If they don't intersect, return null
//Inputs: a (vec3), b (vec3), c (vec3), d (vec3)
//Returns: intersection (vec3) or null if no intersection
//NOTE: When using cramer's rule and the absolute value of the denominator
//of one of the determinants is less than 1e-10, return null to avoid numerical
//precision problems
function getLineSegmentIntersection(a, b, c, d) {
    var ab = vec3.create();
    vec3.subtract(ab, b, a);
    var cd = vec3.create();
    vec3.subtract(cd, d, c);
    
    var res = get3DLineIntersection(a, ab, c, cd);
    if (res === null) {
        return null;
    }
    else if (res.t < 0 || res.t > 1 || res.s < 0 || res.s > 1) {
        //Intersection is outside of the segments
        console.log("t = " + res.t + ", s = " + res.s);
        return null;
    }
    var ret = vec3.clone(a);
    vec3.scaleAndAdd(ret, a, ab, res.t);
    return ret;
}

function getTriNormal(a, b, c) {
    var ab = vec3.create();
    vec3.subtract(ab, b, a);
    var ac = vec3.create();
    vec3.subtract(ac, c, a);
    var N = vec3.create();
    vec3.cross(N, ab, ac);
    vec3.normalize(N, N);
    return N;
}

function getTriangleCircumcenter(a, b, c) {
    //Compute triangle normal as the cross product between ab and ac
    var ab = vec3.create();
    vec3.subtract(ab, b, a);
    var ac = vec3.create();
    vec3.subtract(ac, c, a);
    var N = vec3.create();
    vec3.cross(N, ab, ac);
    vec3.normalize(N, N);
    
    //First perpendicular bisector
    var P = vec3.create(); 
    //Point halfway through ab
    vec3.scaleAndAdd(P, a, ab, 0.5);
    //Direction is cross product between ab and the triangle normal
    var Vp = vec3.create();
    vec3.cross(Vp, N, ab);
    vec3.normalize(Vp, Vp);
    
    //Second perpendicular bisector
    var Q = vec3.create();
    //Point halfway through ac
    vec3.scaleAndAdd(Q, a, ac, 0.5); 
    //Direction is cross product between ac and the triangle normal
    var Vq = vec3.create();
    vec3.cross(Vq, N, ac);
    vec3.normalize(Vq, Vq);

    var ret = get3DLineIntersection(P, Vp, Q, Vq);

    //Compute the radius from one of the points
    var R = vec3.distance(a, ret.P);
    return {Circumcenter:ret.P, Radius:R, P:P, Q:Q, VP:Vp, VQ:Vq};
}

//Purpose: Given four points on a 3D tetrahedron, compute the circumsphere
//by intersecting two perpendicular bisectors from two different triangles,
//and compute the radius of the circumsphere
//Inputs: a (vec3), b (vec3), c (vec3), d (vec3)
//Returns: On object of the form {circumcenter: vec3, R: float (radius)}
function getTetrahedronCircumsphere(a, b, c, d) {
    var c1 = getTriangleCircumcenter(a, b, c).Circumcenter;
    var n1 = getTriNormal(a, b, c);
    var c2 = getTriangleCircumcenter(b, c, d).Circumcenter;
    var n2 = getTriNormal(b, c, d);
    
    var ret = get3DLineIntersection(c1, n1, c2, n2).P;
    console.log("Circumcenter: " + vec3.str(ret));
    var R = vec3.distance(a, ret);
    return {Circumcenter:ret, Radius:R};
}


///////////////////////////////////////////////////////////////////
///********           Plotting Utilities                 *******///
///////////////////////////////////////////////////////////////////

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

//Node.js or browser? Expose methods for unit testing in Node environment
if (typeof window === 'undefined') {
  module.exports = {
    projVector: projVector,
    projPerpVector: projPerpVector,
    getAngle: getAngle,
    getTriangleArea: getTriangleArea,
    getAboveOrBelow: getAboveOrBelow,
    getLineSegmentIntersection: getLineSegmentIntersection,
    getTriangleCircumcenter: getTriangleCircumcenter,
    getTetrahedronCircumsphere: getTetrahedronCircumsphere,
  };
}
