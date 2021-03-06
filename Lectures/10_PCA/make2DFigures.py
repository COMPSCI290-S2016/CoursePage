import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

AW = 0.1
AWV = 0.04
AXW = 0.002

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
    ax.arrow(rx[0], 0, rx[1]-rx[0], 0, head_width = AW, head_length = AW, fc = 'k', ec = 'k', width = AXW)
    ax.arrow(rx[1], 0, rx[0]-rx[1], 0, head_width = AW, head_length = AW, fc = 'k', ec = 'k', width = AXW)
    ax.arrow(0, ry[0], 0, ry[1]-ry[0], head_width = AW, head_length = AW, fc = 'k', ec = 'k', width = AXW)
    ax.arrow(0, ry[1], 0, ry[0]-ry[1], head_width = AW, head_length = AW, fc = 'k', ec = 'k', width = AXW)
    ax.set_xlim((rx[0]-AW, rx[1]+AW))
    ax.set_ylim((ry[0]-AW, ry[1]+AW))
    ax.set_aspect('equal')
    plt.text(rx[1], 0.1, 'X')
    plt.text(0.1, ry[1], 'Y')

def doEigenExamples():
    fSize = [4.5, 4.5]
    axRange = [-0.5, 2.2]
    
    ##SCALES
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[2, 0], [0, 1]])
    u = np.array([1, 0])[:, None]
    v = T.dot(u)
    u = u.flatten()
    v = v.flatten()
    ax.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'b', ec = 'b', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleXEig1.svg', bbox_inches='tight')
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    ax.arrow(0, 0, v[0], v[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleXEig1_T.svg', bbox_inches='tight')
    
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[2, 0], [0, 1]])
    u = np.array([0, 1])[:, None]
    v = T.dot(u)
    u = u.flatten()
    v = v.flatten()
    ax.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'b', ec = 'b', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleXEig2.svg', bbox_inches='tight')
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    ax.arrow(0, 0, v[0], v[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleXEig2_T.svg', bbox_inches='tight')
    
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[2, 0], [0, 1]])
    u = np.array([1, 1])[:, None]
    v = T.dot(u)
    u = u.flatten()
    v = v.flatten()
    ax.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'b', ec = 'b', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleXEig3.svg', bbox_inches='tight')
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    ax.arrow(0, 0, v[0], v[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DScaleXEig3_T.svg', bbox_inches='tight')

    ##SHEARS
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[1, 1], [0, 1]])
    u = np.array([1, 0])[:, None]
    v = T.dot(u)
    u = u.flatten()
    v = v.flatten()
    ax.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'b', ec = 'b', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DShearXEig1.svg', bbox_inches='tight')
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    ax.arrow(0, 0, v[0], v[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DShearXEig1_T.svg', bbox_inches='tight')

    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[1, 1], [0, 1]])
    u = np.array([0, 1])[:, None]
    v = T.dot(u)
    u = u.flatten()
    v = v.flatten()
    ax.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'b', ec = 'b', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DShearXEig2.svg', bbox_inches='tight')
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    ax.arrow(0, 0, v[0], v[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DShearXEig2_T.svg', bbox_inches='tight')


    ##FLIPS
    axRange = [-1.5, 2.5]
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[-1, 0], [0, 2]])
    u = np.array([1, 0])[:, None]
    v = T.dot(u)
    u = u.flatten()
    v = v.flatten()
    ax.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'b', ec = 'b', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipXEig1.svg', bbox_inches='tight')
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    ax.arrow(0, 0, v[0], v[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipXEig1_T.svg', bbox_inches='tight')
    
    axRange = [-1.5, 2.5]
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[-1, 0], [0, 2]])
    u = np.array([1, 1])[:, None]
    v = T.dot(u)
    u = u.flatten()
    v = v.flatten()
    ax.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'b', ec = 'b', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipXEig2.svg', bbox_inches='tight')
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    ax.arrow(0, 0, v[0], v[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipXEig2_T.svg', bbox_inches='tight')

    axRange = [-1.5, 2.5]
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    T = np.array([[-1, 0], [0, 2]])
    u = np.array([0, 1])[:, None]
    v = T.dot(u)
    u = u.flatten()
    v = v.flatten()
    ax.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'b', ec = 'b', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipXEig3.svg', bbox_inches='tight')
    plt.figure(figsize=fSize)
    ax = plt.subplot(111)
    ax.arrow(0, 0, v[0], v[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
    drawAxes(ax, axRange, axRange)
    plt.savefig('2DFlipXEig3_T.svg', bbox_inches='tight')

def doPCAExamples():
    np.random.seed(42)
    N = 1000
    X = np.random.randn(N, 2)
    X = X*(np.random.randn(2))[None, :]
    R = np.random.randn(2, 2)
    [R, S, V] = np.linalg.svd(R)
    X = X.dot(R)
    plt.plot(X[:, 0], X[:, 1], '.')
    plt.axes().set_aspect('equal', 'datalim')
    plt.savefig("2DPCAOrig.svg")
    
    NTrials = 5
    ds = np.zeros(NTrials)
    us = []
    for i in range(NTrials):
        u = np.random.randn(2, 1)
        u = u/np.sqrt(np.sum(u.flatten()**2))
        d = X.dot(u)
        ds[i] = np.sum(d**2)
        us.append(u)
    
    idx = np.argsort(ds)
    A = X.T.dot(X)
    [lams, es] = np.linalg.eig(A)
    print lams
    us.append(es[:, 0])
    us.append(es[:, 1])
    ds = ds.tolist()
    ds.append(lams[0])
    ds.append(lams[1])
    NTrials += 2
    
    idx = idx.tolist()
    idx.append(5)
    idx.append(6)
    for i in range(NTrials):
        u = us[idx[i]]
        d = X.dot(u)
        plt.clf()
        plt.scatter(X[:, 0], X[:, 1], 20, d)
        plt.hold(True)
        u = u.flatten()
        plt.arrow(0, 0, u[0], u[1], head_width = AW, head_length = AW, fc = 'r', ec = 'r', width=AWV)
        plt.title("Summed Squared Dot Prods = %.3g"%np.sum(d**2))
        plt.axes().set_aspect('equal', 'datalim')
        plt.savefig("2DPCADir%i.svg"%i)

if __name__ == '__main__':
    doPCAExamples()
    #doEigenExamples()
