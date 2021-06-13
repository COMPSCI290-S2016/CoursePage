// Steps
// 1. rescale tri2
// 2. compute w based on tri1, tri2
// 3. generate intermediate rectangle (vertex list); how to determine its position?
// 4. cut rectangle to tri1 using lineCut: push rec to cuts first, add transform/hinged with each piece
// 5. cut rectangle to tri2 while "reversing" former cuts
// when to do half cut?



// TODO: fill in input format for triangles
function tri2tri(cuts, tri1, tri2, w) {
	// var S1 = area(tri1);
	// rescale(tri2, S1);
	var r = false;
	if (w === undefined) {
		r = true;
		w4Tri(tri1[0], tri1[1], tri1[2]);
		var w = pick(computeRange(tri1).list[0]);
	}
	var S = triArea(tri1[0], tri1[1], tri1[2]);
	var rec = genRec(S/w, w);
	console.log("width: "+w);
	cuts.push(rec);
	rec2tri(cuts, rec, tri1, false);
	if (r) return;
	rec2tri(cuts, rec, tri2, true);
}

// NOTE: if reverse, p = trans1(p); trans = trans2 * trans1.reverse
// TODO: include rotation/translation
function rec2tri(cuts, rec, tri, invert) {
	// TODO: check tri
	var X = vec3.clone(tri[0]);
	var Y = vec3.clone(tri[1]);
	var Z = vec3.clone(tri[2]);

	if (triCCW(tri)) {
		console.log("CCW"); //debugging
		var A = vec3.clone(rec[0]);// lower left
		var B = vec3.clone(rec[1]);// lower right
		var C = vec3.clone(rec[2]);// upper right
		var D = vec3.clone(rec[3]);// upper left
		var ccw = 1;
	}
	else {
		var B = vec3.clone(rec[0]);// lower left
		var A = vec3.clone(rec[1]);// lower right
		var D = vec3.clone(rec[2]);// upper right
		var C = vec3.clone(rec[3]);// upper left
		var ccw = -1;
	}

	var W = vec3.create(); //vAD
	vec3.subtract(W, D, A);

	var E = vec3.create(); //AB midpoint
	vec3.add(E, A, B);
	vec3.scale(E, E, 0.5);
	var F = vec3.create(); //CD midpoint
	vec3.add(F, E, W);

	// TODO: generalize using cos for parallelogram?
	var l = Math.sqrt(vec3.sqrDist(Y, Z) - vec3.sqrDist(A, B))/2;
	var L = vec3.create();
	vec3.normalize(L, W);
	vec3.scaleAndAdd(L, A, L, l);
	// console.log(vec3.str(L));

	var vEL = vec3.create();
	vec3.subtract(vEL, L, E);
	var f2 = vec3.dot(vEL, W);
	f2 = f2*f2 / vec3.dot(vEL, vEL);
	var m = Math.sqrt(vec3.sqrDist(X, Y)/4 + f2 - vec3.dot(W, W));
	var vZY = vec3.create();
	vec3.subtract(vZY, Y, Z);
	var vYX = vec3.create();
	vec3.subtract(vYX, X, Y);
	if (vec3.dot(vZY, vYX) < 0)
		m = Math.sqrt(f2) - m;
	else
		m = Math.sqrt(f2) + m;
	var M = vec3.create();
	vec3.normalize(M, vEL);
	vec3.scaleAndAdd(M, E, M, m);
	// console.log(vec3.str(M));

	var N = vec3.create();
	vec3.add(N, A, C);
	vec3.subtract(N, N, L);
	// console.log(vec3.str(N));

	var AEL = lineCutSameSide(cuts, E, L, [], A);
	var DFML = lineCutSameSide(cuts, F, M, AEL, D);
	var BEMN = lineCutSameSide(cuts, M, N, AEL, B);

	if (invert) {
		for (var i = 0; i < cuts.length; i++) {
			reverse(cuts[i]);
		}
	}

	var CFMNt = mat4.create();
	var CFMNh = {axis:vec3.create(), angle:0, translation:vec3.create()};
	for (var i = 0; i < cuts.length; i++) {
		var poly = cuts[i];
		if (AEL.indexOf(poly) != -1 || DFML.indexOf(poly) != -1 || BEMN.indexOf(poly) != -1) continue;
		// if (invert) reverse(poly);
		mat4.multiply(poly.transform, CFMNt, poly.transform);
		poly.hinged = cloneHinged(poly.hinged);
		poly.hinged.push(CFMNh);
	}

	var BEMNt = mat4.create();
	var BEMNl = vec3.create();
	vec3.scale(BEMNl, N, 2);
	mat4.translate(BEMNt, BEMNt, BEMNl);
	BEMNt[0] = -1;
	BEMNt[5] = -1;
	var BEMNh = {axis:vec3.clone(N), angle:-Math.PI*ccw, translation:vec3.create()};
	for (var i = 0; i < BEMN.length; i++) {
		var poly = BEMN[i];
		// if (invert) reverse(poly);
		mat4.multiply(poly.transform, BEMNt, poly.transform);
		poly.hinged = cloneHinged(poly.hinged);
		poly.hinged.push(BEMNh);
	}

	var DFMLt = mat4.create();
	var DFMLl = vec3.create();
	vec3.scale(DFMLl, F, 2);
	mat4.translate(DFMLt, DFMLt, DFMLl);
	DFMLt[0] = -1;
	DFMLt[5] = -1;
	var DFMLh = {axis:vec3.clone(F), angle:Math.PI*ccw, translation:vec3.create()};
	for (var i = 0; i < DFML.length; i++) {
		var poly = DFML[i];
		// if (invert) reverse(poly);
		mat4.multiply(poly.transform, DFMLt, poly.transform);
		poly.hinged = cloneHinged(poly.hinged);
		poly.hinged.push(DFMLh);
	}

	var AELt = mat4.create();
	var AELl = vec3.create();
    vec3.subtract(AELl, F, L);
    vec3.scale(AELl, AELl, 2);
    mat4.translate(AELt, AELt, AELl);
    var AELh = {axis:vec3.clone(L), angle:Math.PI*ccw, translation:vec3.create()};
	for (var i = 0; i < AEL.length; i++) {
		var poly = AEL[i];
		// if (invert) reverse(poly);
		mat4.multiply(poly.transform, AELt, poly.transform);
		poly.hinged = cloneHinged(poly.hinged);
		poly.hinged.push(AELh);
		// poly.hinged.push(DFMLh);
		poly.hinged.push({axis:vec3.clone(F), angle:Math.PI*ccw, translation:vec3.create()});
	}

	// apply rotation and translation to match resulting triangle with initial one
	var t = mat4.create();
	var l = vec3.create();

	var vMF = vec3.create();
	var vXY = vec3.create();
	vec3.subtract(vMF, F, M);
	vec3.subtract(vXY, Y, X);
	var a = angle(vMF, vXY);
	vec3.subtract(l, X, M);

    var h = {axis:vec3.clone(M), angle:a, translation:l};
	for (var i = 0; i < cuts.length; i++) {
		var poly = cuts[i];
		poly.hinged = cloneHinged(poly.hinged);
		poly.hinged.push(h);
	}
}

//// Purpose: return the angle used to rotate vector a to vector b
//// Input: vec3 a, b
//// Return: angle
//// TODO: 
function angle(a, b) {
	var cos = vec3.dot(a, b)/(vec3.length(a) * vec3.length(b));
    var angle = Math.acos(cos);
    var cross = vec3.create();
    vec3.cross(cross, a, b);
    if (cross[2] < 0) angle *= -1;
	return angle;
}

//// Purpose: determine whether the triangle is counterclockwise in the plane
//// Input:
//// TODO: move to utility
function triCCW(tri) {
	var ab = vec3.create();
    var ac = vec3.create();
    var cross = vec3.create();
    vec3.subtract(ab, tri[1], tri[0]);
    vec3.subtract(ac, tri[2], tri[0]);
    vec3.cross(cross, ab, ac);
    return cross[2] > 0;
}

//// Purpose: reverse the transform and hinged fields of poly
//// Input:
//// TODO: generalize hinged (currently only 180° works, no translation)
function reverse(poly) {
	transform(poly);
	poly.hinged = cloneHinged(poly.hinged);
	poly.hinged.reverse();
	for (var j = 0; j < poly.hinged.length; j++) {
		var h = poly.hinged[j];
		vec3.add(h.axis, h.axis, h.translation); ////FINAL
		vec3.scale(h.translation, h.translation, -1);
		h.angle *= -1;
	}
}

function transform(polygon) {
    var h = polygon.hinged;
    for (var i = 0; i < polygon.length; i++) {
        var p = polygon[i];
        for (var j = 0; j < h.length; j++) {
            vec3.subtract(p, p, h[j].axis);
            var rotation = mat3.create();
            mat3.rotate(rotation, rotation, h[j].angle);
            vec3.transformMat3(p, p, rotation);
            vec3.add(p, p, h[j].axis);
            vec3.add(p, p, h[j].translation); //translate
        }
    }
}

// TODO? Anchor: lower left or use center? (W, H: width and height vectors?)
function genRec(w, h) {
	var A = vec3.fromValues(400-w/2, 300+h/2, 0);
	var B = vec3.fromValues(400+w/2, 300+h/2, 0);
	var C = vec3.fromValues(400+w/2, 300-h/2, 0);
	var D = vec3.fromValues(400-w/2, 300-h/2, 0);

	var rec = [A, B, C, D];
	rec.transform = mat4.create();
	rec.hinged = [];
	return rec;
}

//// Purpose: helper function for shallow copy of hinged object
//// Input:
//// Return:
function cloneHinged(hinged) {
	var rslt = [];
	for (var i = 0; i < hinged.length; i++) {
		var h = hinged[i];
		h = {axis:vec3.clone(h.axis), angle:h.angle, translation:vec3.clone(h.translation)};
		rslt.push(h);
	}
	return rslt;
}
