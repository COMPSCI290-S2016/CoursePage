f(node, mvMatrix):
    for c in node.children:
        if ('mesh' in node) {
            //Do some stuff if this isn't a dummy node
        }
        f(c, mat4.mul(mvMatrix, node.transform));
