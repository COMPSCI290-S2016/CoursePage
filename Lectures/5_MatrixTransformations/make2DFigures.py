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
    A = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]) #Original Square
    colors = ['r', 'g', 'b', 'k']
    
    axRange = [-0.5, 2.2]
    ##SCALES
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[2, 0], [0, 1]])
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleX.svg', bbox_inches='tight')
    
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[1, 0], [0, 2]])
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleY.svg', bbox_inches='tight')
    
    ###SHEARS
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    plotPoly2D(A, ax, colors)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DShearOrig.svg', bbox_inches='tight')
    
    #Do shear in X
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[1, 1], [0, 1]])
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DShearX.svg', bbox_inches='tight')
    
    #Do shear in Y
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[1, 0], [1, 1]])
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DShearY.svg', bbox_inches='tight')
    
    ##FLIPS
    axRange = [-1.5, 1.5]
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    plotPoly2D(A, ax, colors)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipOrig.svg', bbox_inches='tight') 

    #Do flip around X
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[-1, 0], [0, 1]])
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipX.svg', bbox_inches='tight')

    #Do flip around X and Y
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[-1, 0], [0, -1]])
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipXY.svg', bbox_inches='tight')

    #Scale and flip
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[-1, 0], [0, 1]]).dot(np.array([[2, 0], [0, 1]]))
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, [-2.1, 1], axRange)
    plt.savefig('2DScaleFlip.svg', bbox_inches='tight')
    
    #Skew And Flip
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[-1, 0], [0, 1]]).dot(np.array([[1, 1], [0, 1]]))
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, [-2.1, 1], axRange)
    plt.savefig('2DSkewFlip.svg', bbox_inches='tight')  

    #Flip And Skew
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[1, 1], [0, 1]]).dot(np.array([[-1, 0], [0, 1]]))
    B = (T.dot(A.T)).T
    plotPoly2D(B, ax, colors)
    drawAxes(ax, [-2.1, 1], axRange)
    plt.savefig('2DFlipSkew.svg', bbox_inches='tight')   
