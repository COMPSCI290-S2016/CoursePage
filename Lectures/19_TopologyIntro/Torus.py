import sys
sys.path.append("S3DGLPy")
from Primitives3D import *
from PolyMesh import *

import scipy.sparse
import scipy.stats
import scipy.sparse.linalg as slinalg
import numpy as np
import matplotlib.pyplot as plt


######################################################
##                   Meshes                         ##
######################################################


def getRectMesh(M, N):
    #Create an M x N grid
    idx = np.arange(M*N)
    idx = np.reshape(idx, (M, N))
    [XPos, YPos] = np.meshgrid(np.arange(N), np.arange(M))
    m = PolyMesh()
    for i in range(XPos.size):
        m.addVertex(np.array([XPos.flatten()[i], YPos.flatten()[i], 0]))
    for i in range(M-1):
        for j in range(N-1):
            a = m.vertices[idx[YPos[i, j], XPos[i, j]]]
            b = m.vertices[idx[YPos[i+1, j], XPos[i+1, j]]]
            c = m.vertices[idx[YPos[i+1, j+1], XPos[i+1, j+1]]]
            d = m.vertices[idx[YPos[i, j+1], XPos[i, j+1]]]
            m.addFace([a, b, c])
            m.addFace([a, c, d])
    return m

def getTorusMesh(theta1, theta2, R1, R2):
    M = theta1.size
    N = theta2.size
    [theta1, theta2] = np.meshgrid(theta2, theta1)
    #Create an M x N grid
    idx = np.arange(M*N)
    idx = np.reshape(idx, (M, N))
    [XPos, YPos] = np.meshgrid(np.arange(N), np.arange(M))
    X = (R1 + R2*np.cos(theta1))*np.cos(theta2)
    Y = (R1 + R2*np.cos(theta1))*np.sin(theta2)
    Z = R2*np.sin(theta1)
    m = PolyMesh()
    for i in range(XPos.size):
        m.addVertex(np.array([X.flatten()[i], Y.flatten()[i], Z.flatten()[i]]))
    for i in range(M-1):
        for j in range(N-1):
            i1 = YPos[i, j]
            i2 = (i1+1)%M
            j1 = XPos[i, j]
            j2 = (j1+1)%N
            a = m.vertices[idx[i1, j1]]
            b = m.vertices[idx[i2, j1]]
            c = m.vertices[idx[i2, j2]]
            d = m.vertices[idx[i1, j2]]
            m.addFace([a, b, c])
            m.addFace([a, c, d])
    return m

if __name__ == '__main__':
    theta1 = np.linspace(0, 2*np.pi, 5)
    theta2 = np.linspace(0, 2*np.pi, 5)
    m = getTorusMesh(theta1, theta2, 4, 1)
    m.saveOffFile("torus.off")
