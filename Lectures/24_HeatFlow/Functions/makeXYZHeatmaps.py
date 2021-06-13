import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../S3DGLPy")
from Primitives3D import *
from PolyMesh import *
from LaplacianMesh import *
from scipy import sparse
import scipy.io as sio
from scipy.sparse.linalg import lsqr, cg, eigsh
import os

#this_path = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, this_path + '/ext/libigl/python/')
#sys.path.insert(0, this_path + '/ext/lib/')
#import igl

if __name__ == '__main__':
    NBasis = 500
    cmap = plt.get_cmap('jet')

    (VPos, VColors, ITris) = loadOffFileExternal("teapot.off")
    
    XYZ = VPos - np.min(VPos, 0)[None, :]
    XYZ = XYZ / np.max(XYZ, 0)[None, :]
    VColors = cmap(XYZ[:, 0])[:, 0:3]*255
    VColors = np.round(VColors)
    saveOffFileExternal("meshX.off", VPos, VColors, ITris)
    VColors = cmap(XYZ[:, 1])[:, 0:3]*255
    VColors = np.round(VColors)
    saveOffFileExternal("meshY.off", VPos, VColors, ITris)
    VColors = cmap(XYZ[:, 2])[:, 0:3]*255
    VColors = np.round(VColors)
    saveOffFileExternal("meshZ.off", VPos, VColors, ITris)
