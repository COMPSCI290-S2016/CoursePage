import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


import sys
sys.path.append('G-RFLCT')
from Primitives3D import *
from Graphics3D import *
from PolyMesh import *
from Cameras3D import *
from EMScene import *
from RayTraceImage import *

AW = 0.1

def plotPoly2D(A, ax, colors):
    ax.hold(True)
#    for i in range(A.shape[0]):
#        j = (i+1)%A.shape[0]
#        plt.plot(A[[i, j], [0, 0]], A[[i, j], [1, 1]], 'k')
    ax.add_patch(Polygon(A, linestyle='solid', color='#FFBBBB'))
    for i in range(A.shape[0]):
        ax.scatter(A[i, 0], A[i, 1], 60, colors[i])
    ax.grid()

def plotEMPoly(scene):
    

def drawAxes(ax, rx, ry):
    ax.arrow(rx[0], 0, rx[1]-rx[0], 0, head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    ax.arrow(rx[1], 0, rx[0]-rx[1], 0, head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    ax.arrow(0, ry[0], 0, ry[1]-ry[0], head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    ax.arrow(0, ry[1], 0, ry[0]-ry[1], head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    ax.set_xlim((rx[0]-AW, rx[1]+AW))
    ax.set_ylim((ry[0]-AW, ry[1]+AW))
    ax.set_aspect('equal')
    plt.text(rx[1], 0.1, 'X')
    plt.text(0.1, ry[1], 'Y')

if __name__ == '__main__':
    scene = EMScene()
    scene.Read('test.xml')
    fSize = [4.5, 4.5]    
    
    for p in scene.paths:
        x = []
        for v in p:
            x.append([v.x, v.y])
        x = np.array(x)
        plt.plot(x[:, 0], x[:, 1])
        plt.show()
        
    
#    ##SCALES
#    plt.figure(figsize=fSize)
#    ax = plt.subplot(111)
#    theta = np.pi/6
#    T = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
#    G = np.linalg.inv(T.T)
#    B = (T.dot(A.T)).T
#    P2 = (T.dot(P[:, None])).flatten()
#    N2 = (T.dot(N[:, None])).flatten()
#    N3 = (G.dot(N[:, None])).flatten()
#    plotPoly2D(B, ax, colors)
#    ax.arrow(P2[0], P2[1], 0.3*N2[0], 0.3*N2[1], head_width = AW, head_length = AW, fc = 'k', ec = 'k')
#    drawAxes(ax, axRange, axRange)
#    plt.savefig('2DRotateNormal.svg', bbox_inches='tight')
