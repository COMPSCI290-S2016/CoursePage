// data structure and utility functions for closed real intervals

function computeRange(tri) {
	var S = triArea(tri[0], tri[1], tri[2]);

    var totalR = [];
    var listR = [];
	for (var i = 0; i < 3; i++) {
		var A = tri[i];
		var B = tri[(i+1)%3];
		var C = tri[(i+2)%3];

		var aH = vec3.distance(B, C)/2;
		var hH = S/vec3.distance(B, C);
		if (aH-hH*2 > 0) {
			var x1 = (Math.sqrt(aH*(aH+hH*2))-Math.sqrt(aH*(aH-hH*2)))/2;
			var x2 = (Math.sqrt(aH*(aH+hH*2))+Math.sqrt(aH*(aH-hH*2)))/2;
			var validR = [{inf:hH, sup:x1}, {inf:x2, sup:Infinity}];
		}
		else {
			var validR = [{inf:hH, sup:Infinity}];
		}
		for (var j = 0; j < 2; j++) {
			var vAB = vec3.create();
			vec3.subtract(vAB, B, A);
			var vCB = vec3.create();
			vec3.subtract(vCB, B, C);
			var k = vec3.dot(vAB, vCB)/vec3.dot(vCB, vCB);
			if (k < -1) {
				listR.push([]);
				swap(B, C);
				continue;
			}
			var BF = vec3.distance(A, B)/2;
			var BE = Math.sqrt(vec3.sqrDist(A, B)/2 + vec3.sqrDist(B, C)/2 - vec3.sqrDist(A, C)/4);
			if (k < 0) {
				var currR = intersect(validR, range(-Infinity, BE));
			}
			else {
				var currR = intersect(validR, range(BF, BE));
			}
			listR.push(currR);
			totalR = union(totalR, currR);
			swap(B, C);
		}
	}
	return {total:totalR, list:listR};
}

function range(a, b) {
	return [{inf:a, sup:b}];
}

function complement(range) {
	var rslt = [];
	if (range.length == 0) return [{inf:-Infinity, sup:Infinity}];
	if (range[0].inf != -Infinity) rslt.push({inf:-Infinity, sup:range[0].inf});
	for (var i = 0; i < range.length-1; i++) {
		rslt.push({inf:range[i].sup, sup:range[i+1].inf});
	}
	if (range[range.length-1].sup != Infinity) rslt.push({inf:range[range.length-1].sup, sup:Infinity});
	return rslt;
}

function intersect(range1, range2) {
	var range = [];
	for (var i = 0; i < range1.length; i++) {
		var R1 = range1[i];
		for (var j = 0; j < range2.length; j++) {
			var R2 = range2[j];
			var inf = Math.max(R1.inf, R2.inf);
			var sup = Math.min(R1.sup, R2.sup);
			if (inf <= sup) range.push({inf:inf, sup:sup});
		}
	}
	return range;
}

function union(range1, range2) {
	for (var i = 0; i < range1.length; i++) {
		var range = [];
		var R1 = range1[i];
		var infIndex = -1;
		var supIndex = range2.length;
		for (var j = 0; j < range2.length; j++) {
			var R2 = range2[j];
			if (infIndex == -1 && R1.inf <= R2.sup) {
				infIndex = j;
			}
			if (R1.sup >= R2.inf) {
				supIndex = j;
			}
		}
		if (infIndex == -1) {
			range2.push(R1);
		}
		else if (supIndex == range2.length) {
			range2.splice(0, 0, R1);
		}
		else {
			for (var k = 0; k < infIndex; k++) {
				range.push(range2[k]);
			}
			var inf = Math.min(R1.inf, range2[infIndex].inf);
			var sup = Math.max(R1.sup, range2[supIndex].sup);
			range.push({inf:inf, sup:sup});
			for (var k = supIndex+1; k < range2.length; k++) {
				range.push(range2[k]);
			}
			range2 = range;
		}
	}
	return range2;
}

function within(x, range) {
	for (var i = 0; i < range.length; i++) {
		if (x >= range[i].inf && x <= range[i].sup) return true;
	}
	return false;
}

function pick(range) {
	var l = Math.floor(range.length/2);
	return (range[l].inf + range[l].sup)/2;
}

function print(range) {
	var str = "";
	for (var i = 0; i < range.length; i++) {
		str += "["+range[i].inf.toFixed(2)+","+range[i].sup.toFixed(2)+"] ";
	}
	console.log(str);
}
