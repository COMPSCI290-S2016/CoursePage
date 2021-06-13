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
    NBasis = 800
    cmap = plt.get_cmap('Spectral')
    filename = 'me'
    
    (VPos, VColors, ITris) = loadOffFileExternal('%s.off'%filename)
    #VPos = VPos + 0.003*np.random.randn(VPos.shape[0], VPos.shape[1])
    #saveOffFileExternal("%sNoise.off"%filename, VPos, np.array([]), ITris)
    
#    VPosE = igl.eigen.MatrixXd(VPos)
#    ITrisE = igl.eigen.MatrixXi(ITris)
#    L = igl.eigen.SparseMatrixd()
#    igl.cotmatrix(VPosE,ITrisE,L)
#    coo = np.array(L.toCOO())
#    I = coo[:, 0]
#    J = coo[:, 1]
#    V = coo[:, 2]
#    L = sparse.coo_matrix((V,(I,J)), shape=(L.rows(),L.cols()), dtype='float64')

    L = makeLaplacianMatrixUmbrellaWeights(VPos, ITris, [])

    (eigvalues, eigvectors) = eigsh(L, NBasis, sigma = 0, which='LM')
#    sio.savemat("homerupeigs.mat", {"eigvalues":eigvalues})
#    for k in range(NBasis):
#        Y = np.zeros(L.shape[0])
#        if k > 0:
#            Y = eigvectors[:, k]
#            Y = Y - np.min(Y)
#            Y = Y/np.max(Y)
#        VColors = np.array(np.round(255.0*cmap(Y)[:, 0:3]), dtype=np.int64)
#        saveOffFileExternal("%s%i.off"%(filename, k), VPos, VColors, ITris)
    
    VPos = eigvectors.dot(eigvectors.T.dot(VPos))
    saveOffFileExternal("%s_Proj%i.off"%(filename, NBasis), VPos, np.array([]), ITris)
