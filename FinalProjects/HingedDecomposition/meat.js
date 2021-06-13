function entryPoint(cuts1, cuts2, cuts, A, B, C, D, E, F) {
    triRescale(triArea(A, B, C), D, E, F, null);
    // w4Tri(A, B, C);
    w4Tri(D, E, F);
    var R1 = computeRange([A, B, C]);
    var R2 = computeRange([D, E, F]);
    var intxn = intersect(R1.total, R2.total);
    print(intxn);

    var count = 0;
    var increment = 1;
    var Dt = vec3.clone(D);
    var vFE = vec3.create();
    vec3.subtract(vFE, E, F);
    while (intxn.length == 0) {
    	vec3.scaleAndAdd(Dt, Dt, vFE, increment);
    	count -= increment;
    	R2 = computeRange([Dt, E, F]);
    	if (R2.list[0].length == 0) {
    		console.log("count "+count);
    		increment = -1;
    		Dt = vec3.clone(D);
    		count = 0;
    	}
    	else intxn = intersect(R1.total, R2.list[0]);
    	if (Math.abs(count) > 1000) {
    		console.log("triangle 2 too tall");
    		return;
    	}
    }
    var x = pick(intxn);
    var index = -1;
    for (var i = 0; i < R1.list.length; i++) {
    	if (within(x, R1.list[i])) {
    		var index = i;
    		break;
    	}
    }
    console.log("count: "+count);
    var tri1 = [A, B, C];
    var k = Math.floor(index/2);
    tri1 = [tri1[k], tri1[(k+1)%3], tri1[(k+2)%3]];
    if (index%2 == 1) swap(tri1[1], tri1[2]);

    vec3.copy(D, Dt); //
    var tri2 = [D, E, F];
    if (count == 0) {
    	index = -1;
    	for (var j = 0; j < R2.list.length; j++) {
    		if (within(x, R2.list[j])) {
    			var index = j;
    			break;
    		}
    	}
    	k = Math.floor(index/2);
    	tri2 = [tri2[k], tri2[(k+1)%3], tri2[(k+2)%3]];
    	if (index%2 == 1) swap(tri2[1], tri2[2]);
    }
    // test(cuts1, tri1, x, 0);
    // test(cuts2, tri2, x, count);
    tri2tri(cuts, tri1, tri2, x);
}

function test(cuts, tri, x, l) {
    var A = tri[0];
    var B = tri[1];
    var C = tri[2];
    var vCB = vec3.create();
    vec3.subtract(vCB, B, C);
    
    vec3.scaleAndAdd(A, A, vCB, -l);
    cutTri2Rec(cuts, A, B, C, x);

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
