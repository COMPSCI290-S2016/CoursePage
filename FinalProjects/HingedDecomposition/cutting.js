
// Cut with line cd, and return indices of cuts on the same side of cd as A
function lineCutSameSide(cuts, c, d, ignore, A) {
    var sameSideIndices = [];
    var sameSide = [];
    for (var i = 0; i < cuts.length; i++) {
        if (ignore.indexOf(cuts[i]) != -1) continue;
        var lineCut = lineCutPoly(cuts[i], c, d, A);
        if (lineCut.same0) {
            sameSideIndices.push(i);
        }
        if (lineCut.pieces != null) {
            cuts.splice(i, 1, lineCut.pieces[0], lineCut.pieces[1]);
            i++;
            if (!lineCut.same0) {
                sameSideIndices.push(i);
            }
        }
    }
    for (var i = 0; i < sameSideIndices.length; i++) {
        sameSide.push(cuts[sameSideIndices[i]]);
    }
    return sameSide;
}

function lineCutPoly(polygon, c, d, A) {
    var intxn1 = null;
    var intxn2 = null;
    var index1 = -1;
    var index2 = -1;
    var intxn1IsVertex = false;
    var intxn2IsVertex = false;
    var sideIndex = -1;
    var same = false;
    var toBreak = false;
    for (var i = 0; i < polygon.length; i++) {
        var rslt = lineIntersection(polygon[i], polygon[(i+1)%polygon.length], c, d);
        if (rslt != null) {
            if (intxn1 === null) {
                if (rslt.isVertex) {
                    intxn1IsVertex = true;
                }
                intxn1 = rslt.intxn;
                index1 = i;
            } else if (intxn2 === null) {
                if (rslt.isVertex) {
                    if (intxn1IsVertex && ((i - index1) == 1 || (i - index1) == (polygon.length-1))) {
                        if (sideIndex != -1) break;
                        toBreak = true;
                        continue;
                    }
                    intxn2IsVertex = true;
                }
                intxn2 = rslt.intxn;
                index2 = i;
                toBreak = true;
            }
        } else if (sideIndex == -1) {
            sideIndex = i;
            var dc = vec3.create();
            vec3.subtract(dc, c, d);
            var dA = vec3.create();
            vec3.subtract(dA, A, d);
            var perp = vec3.create();
            vec3.subtract(perp, dA, proj(dc, dA));
            var dP = vec3.create();
            vec3.subtract(dP, polygon[i], d);
            same = (vec3.dot(dP, perp) > 0);

            var dot = vec3.dot(dP, perp); if (Math.abs(dot) < 0.1) console.log("numerical precision warning!");// console.log("dot " + dot);
        }
        if (toBreak && sideIndex != -1) break;
    }
    if (intxn2 === null) {
        return {same0:same, pieces:null};
    }
    if (sideIndex < index1 || sideIndex > index2) {
        same = (!same);
    }

    var cut1 = [];
    cut1.transform = mat4.clone(polygon.transform); //
    cut1.hinged = polygon.hinged;
    cut1.push(vec3.clone(intxn1));
    var i = index1;
    while (i != index2) {
        i = (i+1)%polygon.length;
        cut1.push(vec3.clone(polygon[i])); //
    }
    if (!intxn2IsVertex) cut1.push(vec3.clone(intxn2));

    var cut2 = [];
    cut2.transform = mat4.clone(polygon.transform); //
    cut2.hinged = polygon.hinged;
    cut2.push(vec3.clone(intxn2));
    var j = index2;
    while (j != index1) {
        j = (j+1)%polygon.length;
        cut2.push(vec3.clone(polygon[j])); //
    }
    if (!intxn1IsVertex) cut2.push(vec3.clone(intxn1));

    return {same0:same, pieces:[cut1, cut2]};
}

// TODO: a better way for 3D?
// Find the intersection of segment ab and line cd
// Note: intersection is allowed at a but forbidden at b (0 <= s < 1)
function lineIntersection(a, b, c, d) {
    var eps = 0.001;// Temporary sol'n to numerical precision problem
    var ab = vec3.create();
    var cd = vec3.create();
    vec3.subtract(ab, b, a);
    vec3.subtract(cd, d, c);
    var det = -ab[0]*cd[1]+ab[1]*cd[0];
    var s = (-(c[0]-a[0])*cd[1]+(c[1]-a[1])*cd[0])/det;
    if (det == 0) {
        det = -ab[2]*cd[1]+ab[1]*cd[2];
        if (det == 0) return null;
        s = (-(c[2]-a[2])*cd[1]+(c[1]-a[1])*cd[2])/det;
    }

    if (Math.abs(s) < eps) return {intxn:a, isVertex:true};
    if (s < 0 || s >= 1-eps) return null;
    var rslt = vec3.create();
    vec3.scale(rslt, ab, s);
    vec3.add(rslt, rslt, a);
    return {intxn:rslt, isVertex:false};
}
