var mesh = node.mesh;
//Loop through faces
for (var f = 0; f < mesh.faces.length; f++) {
    //"Pointer" to face
    var face = mesh.faces[f];
    //For each face get vertices in CCW order
    var verts = face.getVerticesPos();
    //Do stuff with the vertices...
}
