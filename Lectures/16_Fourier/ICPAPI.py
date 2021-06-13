def getCentroid(PC):
    return np.zeros((3, 1)) #Dummy value

def getCorrespondences(X, Y, Cx, Cy, Rx):
    return np.zeros(X.shape[1], dtype=np.int64) #dummy value

def getProcrustesAlignment(X, Y, idx):
    return (Cx, Cy, R)    

#what the ICP algorithm did
def doICP(X, Y, MaxIters):
    CxList = [np.zeros((3, 1))]
    CyList = [np.zeros((3, 1))]
    RxList = [np.eye(3)]
    #TODO: Fill the rest of this in    
    return (CxList, CyList, RxList)
