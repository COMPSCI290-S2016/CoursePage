// Return the projection of b onto a
function proj(a, b) {
    var out = vec3.clone(a);
    var k = vec3.dot(a, a);
    if (k > 0) {
        k = vec3.dot(a, b) / k;
        vec3.scale(out, a, k);
    }
    return out;
}

function swap(B, C) {
    var temp = vec3.clone(B);
    vec3.copy(B, C);
    vec3.copy(C, temp);
}

function same(B, C) {
    var d2 = vec3.sqrDist(B, C);
    if (d2 != 0 && d2 < 0.05) {
        console.log("same? " + d2);
        console.log(vec3.str(B));
        console.log(vec3.str(C));
    }
    return vec3.sqrDist(B, C)==0;
}

// Return the area of triangle ABC
function triArea(a, b, c) {
    var ab = vec3.create();
    var ac = vec3.create();
    var cross = vec3.create();
    vec3.subtract(ab, b, a);
    vec3.subtract(ac, c, a);
    vec3.cross(cross, ab, ac);
    return vec3.length(cross)/2;
}

// Z is the optional zoom point; default is A?
function triRescale(area, A, B, C, Z) {
    var k = Math.sqrt(area/triArea(A, B, C));
    if (Z === null) Z = A; //

    var ZP = vec3.create();
    var tri = [A, B, C];
    for (var i = 0; i < tri.length; i++) {
        vec3.subtract(ZP, tri[i], Z);
        vec3.scale(ZP, ZP, k);
        vec3.add(tri[i], Z, ZP);
    }
}
