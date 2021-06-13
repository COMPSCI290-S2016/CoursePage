
// TODO: write a function to generalize (to 3D, in one place, including translation)
// is "if (null)" better in performance??
function drawPoly(ctx, polygon, t) {
    var transforms = [];
    if (t > 0) {
        for (var i = 0; i < polygon.hinged.length; i++) {
            var x = polygon.hinged[i].translation;
            var rotation = mat3.create();
            mat3.rotate(rotation, rotation, polygon.hinged[i].angle * t);
            var translation = vec3.create();
            vec3.scale(translation, polygon.hinged[i].translation, t);
            transforms.push({axis:polygon.hinged[i].axis, rotation:rotation, translation:translation});
        }
    }

    ctx.beginPath();
    for (var i = 0; i < polygon.length; i++) {
        var p = vec3.clone(polygon[i]);
        // if (!('transform' in polygon)) {ctx.fillStyle = "#000000"; ctx.fillText(["A","B","C"][i], p[0], p[1]);}
        for (var j = 0; j < transforms.length; j++) {
            vec3.subtract(p, p, transforms[j].axis);
            vec3.transformMat3(p, p, transforms[j].rotation);
            vec3.add(p, p, transforms[j].axis);
            vec3.add(p, p, transforms[j].translation); //translate
        }
        // else vec3.transformMat4(p, p, polygon.transform);
        if (i == 0) ctx.moveTo(p[0], p[1]);
        else ctx.lineTo(p[0], p[1]);
    }
    ctx.closePath();
    if ('transform' in polygon) {
        if (!('color' in polygon)) polygon.color = randomColor();
        ctx.fillStyle = polygon.color;
        ctx.fill();
    }
    else //
        ctx.stroke();
}

function drawPolygons(ctx, polygons, t) {
    for (var i = 0; i < polygons.length; i++) {
        drawPoly(ctx, polygons[i], t);
    }
}

function randomColor() {
    var hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'];
    var color = "#";
    for (var i = 0; i < 6; i++) {
        var h = Math.floor(Math.random()*16);
        color += hex[h];
    }
    return color;
}

function insidePolygon(P, transformed) {
    var ref = crossProduct(transformed[transformed.length-1], transformed[0], P);
    for (var i = 0; i < transformed.length-1; i++) {
        if (vec3.dot(ref, crossProduct(transformed[i], transformed[i+1], P)) <= 0) {
            //// no intersection if P on the line of an edge (when crossProduct==0)
            return false;
        }
    } 
    return true;
}

//// Helper funtion to find the cross product of two vec3's AB and AC
function crossProduct(A, B, C) {
    var ab = vec3.create();
    var ac = vec3.create();
    var crs = vec3.create();
    vec3.subtract(ab, B, A);
    vec3.subtract(ac, C, A);
    vec3.cross(crs, ab, ac);
    return crs;
}


