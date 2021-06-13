// Purpose: equidecomposition original algorithms

//// Status: Working
// TODO: return the resulting rectangle?
function cutTri2Rec(cuts, A, B, C, w, V) {
    V = null;
    A = vec3.clone(A);
    B = vec3.clone(B);
    C = vec3.clone(C);
    var vAB = vec3.create();
    vec3.subtract(vAB, B, A);
    var vCA = vec3.create();
    vec3.subtract(vCA, A, C);
    var vCB = vec3.create();
    vec3.subtract(vCB, B, C);
    var a = vec3.length(vCB);

    var vCE = vec3.create(); //may not needed
    vec3.scale(vCE, vCA, 0.5);
    var E = vec3.create();
    vec3.add(E, C, vCE);
    var vCH = proj(vCB, vCE);
    var vEH = vec3.create();
    vec3.subtract(vEH, vCH, vCE);
    if (w < vec3.length(vEH)) { //if = , ABC > pi/2 and NXY=0
        console.log("w < EH: w="+w+" EH="+vec3.length(vEH));
        return;
    }
    var vHX = vec3.create();
    vec3.normalize(vHX, vCB);
    vec3.scale(vHX, vHX, Math.sqrt(w*w - vec3.dot(vEH, vEH)));
    var vCX = vec3.create();
    vec3.add(vCX, vCH, vHX);
    if (vec3.length(vCX) < a/2 || vec3.length(vCX) > a) { //if = , CY=0 or BX=0
        var BF = vec3.distance(A, B)/2;
        var BE = Math.sqrt(vec3.sqrDist(A, B)/2 + vec3.sqrDist(B, C)/2 - vec3.sqrDist(A, C)/4);
        console.log("X outside BD: w="+w+" BF="+BF+" BE="+BE);
        return;
    }
    var X = vec3.create();
    vec3.add(X, C, vCX);

    var F = vec3.create();
    vec3.scaleAndAdd(F, A, vAB, 0.5);
    var Y = vec3.create();
    vec3.scaleAndAdd(Y, X, vCB, -0.5);

    var EX = vec3.create();
    vec3.subtract(EX, X, E);
    var EF = vec3.create();
    vec3.subtract(EF, F, E);
    var EM = proj(EX, EF);
    var M = vec3.create();
    vec3.add(M, E, EM);
    if(vec3.length(EM) > vec3.length(EX)) {
        console.log("M outside EX: EM="+vec3.length(EM)+" EX="+vec3.length(EX));
        return;
    }
    var N = vec3.create();
    vec3.subtract(N, X, EM);
    var translationTEMP = vec3.create();
    if (V != null && V != undefined) vec3.subtract(translationTEMP, V, M);


    var AFME = [A, F, M, E];
    cuts.push(AFME);
    AFME.transform = mat4.create();

    AFME.axis = vec3.create();
    AFME.angle = 0;
    AFME.translation = vec3.create();
    AFME.hinged = [{axis:vec3.create(), angle:0, translation:translationTEMP}];


    var BXMF = [B, X, M, F];
    cuts.push(BXMF);
    var tBXMF = vec3.create();
    vec3.scale(tBXMF, F, 2);
    BXMF.transform = mat4.create();
    mat4.translate(BXMF.transform, BXMF.transform, tBXMF);
    // mat4.rotateZ(BXMF.transform, BXMF.transform, Math.PI);
    BXMF.transform[0] = -1;
    BXMF.transform[5] = -1;

    BXMF.axis = F;
    BXMF.angle = Math.PI; //
    // temp sol'n for 2D hinged dissection
    var cross = vec3.create();
    vec3.cross(cross, vCA, vCB);
    if (vec3.dot(cross, vec3.fromValues(0,0,1)) > 0) BXMF.angle *= -1;
    BXMF.translation = vec3.create();
    BXMF.hinged = [{axis:vec3.clone(F), angle:BXMF.angle, translation:translationTEMP}];


    var CENY = [C, E, N, Y];
    cuts.push(CENY);
    var tCENY = vec3.create();
    vec3.scale(tCENY, E, 2);
    CENY.transform = mat4.create();
    mat4.translate(CENY.transform, CENY.transform, tCENY);
    CENY.transform[0] = -1;
    CENY.transform[5] = -1;

    CENY.axis = E;
    CENY.angle = -BXMF.angle; //
    CENY.translation = vec3.create();
    CENY.hinged = [{axis:vec3.clone(E), angle:-BXMF.angle, translation:translationTEMP}];


    var NXY = [N, X, Y];
    cuts.push(NXY);
    var tNXY = vec3.create();
    vec3.subtract(tNXY, F, X);
    vec3.scale(tNXY, tNXY, 2);
    NXY.transform = mat4.create();
    mat4.translate(NXY.transform, NXY.transform, tNXY);

    NXY.attachedTo = CENY; //BXMF
    NXY.axis = Y; //X
    NXY.angle = NXY.attachedTo.angle; //TODO: generalize this?
    NXY.translation = vec3.create();
    NXY.hinged = [{axis:vec3.clone(Y), angle:-BXMF.angle, translation:vec3.create()}, CENY.hinged[0]];

    var tmp = vec3.create();
    vec3.transformMat4(tmp, F, CENY.transform);
    var tm = vec3.create();
    vec3.subtract(tm, A, vCB);
    vec3.add(tm, tm, C);
    vec3.scale(tm, tm, 0.5);
}

// make an object {tri} and store with it info about sides?
// TODO: clean up overlapping code with w4Tri()
function nameLater(A, B, C, w) {
    var vAB = vec3.create();
    vec3.subtract(vAB, B, A);
    var vCB = vec3.create();
    vec3.subtract(vCB, B, C);
    var aH = vec3.length(vCB)/2;
    var hH = triArea(A, B, C)/vec3.length(vCB); //hH := h_a/2
    if (aH-hH*2 > 0) {
        var temp1 = Math.sqrt(aH*(aH+hH*2));
        var temp2 = Math.sqrt(aH*(aH-hH*2));
        var x1 = (temp1-temp2)/2;
        var x2 = (temp1+temp2)/2;
        if (w < hH || (w > x1 && w < x2)) {
            console.log("invalid w");
            return;
        }
    }
    var kw = Math.sqrt(w*w - hH*hH)/aH;

    var k = vec3.dot(vAB, vCB)/vec3.dot(vCB, vCB);

    if (k < -1) {
        k = 1 - k;
        swap(B, C);
    }
    else if (k < 0.5) {
        if (kw >= k && kw <= k+1) { //kw in [k, k+1]
            return 0;
        }
        // if (kw < k) return -1; //k in (0, 0.5) & kw in [k-1, k) --optional swap; always -1
        if (k <= -0.5 && kw <= k+2) return 1; //k in [-1, -0.5] & kw in (k+1, k+2]
        k = 1 - k;
        swap(B, C);
    }
    else if (k >= 1.5 && k <= 2 && kw >= 2-k && kw <= 3-k) {
        swap(B, C);
        return 1;
    }
    // for now it seems better to return negative?
    if (kw < k)
        return Math.floor(kw-k);
    if (kw > k+1)
        return Math.ceil(kw-k-1);
    return 0;
}

// Return a valid(/TODO: optimal?) w for the triangle(s?) ABC; swap if necessary
function w4Tri(A, B, C) {
    if (vec3.distance(A, C) < vec3.distance(B, C)) swap(A, B);
    if (vec3.distance(A, B) < vec3.distance(B, C)) swap(A, C);
    if (vec3.distance(A, B) < vec3.distance(A, C)) swap(B, C); //optional
    var aH = vec3.distance(B, C)/2;
    var hH = triArea(A, B, C)/vec3.distance(B, C);
    if (aH-hH*2 > 0)
        var hH = (Math.sqrt(aH*(aH+hH*2))+Math.sqrt(aH*(aH-hH*2)))/2;
    return hH+50; //TODO: check numerical precision!
}

function testTri2Rec(cuts, tri, w, V) {
    var A = tri[0];
    var B = tri[1];
    var C = tri[2];
    if (w === null) w = w4Tri(A, B, C); //for testing only
    var l = nameLater(A, B, C, w);
    //// console.log(l);
    var vCB = vec3.create();
    vec3.subtract(vCB, B, C);
    
    vec3.scaleAndAdd(A, A, vCB, -l);
    cutTri2Rec(cuts, A, B, C, w, V);

    var Btemp = vec3.clone(B);
    var Ctemp = vec3.clone(C);
    if (l > 0) {
        swap(Btemp, Ctemp);
        vec3.scale(vCB, vCB, -1);
    }
    for (var m = 0; m < Math.abs(l); m++) {
        var E = vec3.create();
        vec3.add(E, A, Ctemp);
        vec3.scale(E, E, 0.5);
        var sameSide = lineCutSameSide(cuts, Btemp, E, [], A);

        var temp = vec3.create();
        vec3.scale(temp, E, 2);
        var transform = mat4.create();
        mat4.translate(transform, transform, temp);
        transform[0] = -1;
        transform[5] = -1;
        for (var i = 0; i < sameSide.length; i++) {
            var poly = sameSide[i];
            for (var k = 0; k < poly.length; k++) {
                vec3.transformMat4(poly[k], poly[k], transform);
            }
            mat4.multiply(poly.transform, poly.transform, transform);
            var temp = cloneHinged(poly.hinged);
            poly.hinged = [{axis:vec3.clone(E), angle:-Math.PI, translation:vec3.create()}];
            for (var n = 0; n < temp.length; n++) {
                poly.hinged.push(temp[n]);
            }
        }
        vec3.subtract(A, A, vCB);
    }
}

// Currently testing only; doCut() entry point
function cutTri2Tri(cuts1, cuts2, cuts, A, B, C, D, E, F) {
    triRescale(triArea(A, B, C), D, E, F, null);
    var w1 = w4Tri(A, B, C);
    var w2 = w4Tri(D, E, F);
    var w = Math.max(w1, w2);
    testTri2Rec(cuts1, [A, B, C], w, vec3.fromValues(400, 150, 0));
    testTri2Rec(cuts2, [D, E, F], w, vec3.fromValues(400, 450, 0));
}
