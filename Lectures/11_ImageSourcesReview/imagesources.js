scene.imsources = [scene.source];
for (order = 1:k):
    for s in scene.imsources:
        if s.order == order-1 {
            //Reflect (call recursive scene tree function)
            //Generate a bunch of images snew
            snew.parent = s
            snew.genFace = face reflected
        }
