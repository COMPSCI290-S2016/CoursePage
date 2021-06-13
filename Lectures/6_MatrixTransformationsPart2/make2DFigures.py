import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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
    fSize = [4.5, 4.5]
    axRange = [-0.5, 2.2]
    A = np.array([[0, 0], [1, 0], [0, 1]]) #Original Triangle
    P = np.array([0.5, 0.5])
    N = np.array([1, 1])
    colors = ['r', 'g', 'b']
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    plotPoly2D(A, ax, colors)
    drawAxes(ax, axRange, axRange)
    #Draw Normal
    ax.arrow(P[0], P[1], 0.3*N[0], 0.3*N[1], head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    plt.savefig('2DTriOrigNormal.svg', bbox_inches='tight')
    
    
    ##SCALES
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    theta = np.pi/6
    T = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    G = np.linalg.inv(T.T)
    B = (T.dot(A.T)).T
    P2 = (T.dot(P[:, None])).flatten()
    N2 = (T.dot(N[:, None])).flatten()
    N3 = (G.dot(N[:, None])).flatten()
    plotPoly2D(B, ax, colors)
    ax.arrow(P2[0], P2[1], 0.3*N2[0], 0.3*N2[1], head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DRotateNormal.svg', bbox_inches='tight')
    
    ##SCALES
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[2, 0], [0, 1]])
    G = np.linalg.inv(T.T)
    print G
    B = (T.dot(A.T)).T
    P2 = (T.dot(P[:, None])).flatten()
    N2 = (T.dot(N[:, None])).flatten()
    N3 = (G.dot(N[:, None])).flatten()
    plotPoly2D(B, ax, colors)
    ax.arrow(P2[0], P2[1], 0.3*N2[0], 0.3*N2[1], head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleXNormal.svg', bbox_inches='tight')
    
    #Now save correct normal
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    plotPoly2D(B, ax, colors)
    ax.arrow(P2[0], P2[1], 0.3*N3[0], 0.3*N3[1], head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleXNormalCorrect.svg', bbox_inches='tight')
    
    ##SkewScale
    T = np.array([[1.5, 1], [0, 1]])
    G = np.linalg.inv(T.T)
    print G
    B = (T.dot(A.T)).T
    P2 = (T.dot(P[:, None])).flatten()
    N2 = (T.dot(N[:, None])).flatten()
    N3 = (G.dot(N[:, None])).flatten()
    
    #Now save correct normal
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    plotPoly2D(B, ax, colors)
    ax.arrow(P2[0], P2[1], 0.3*N3[0], 0.3*N3[1], head_width = AW, head_length = AW, fc = 'k', ec = 'k')
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleSkewNormal.svg', bbox_inches='tight')
