import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

AW = 0.05

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
    np.random.seed(100)
    axRange = [-1, 2.2]
    fSize = [12, 6]
    
    NPoints = 4
    X = np.random.rand(NPoints, 2)
    #Apply a little bit of noise and a random rotation
    Y = X + 0.1*np.random.randn(NPoints, 2)
#    R = np.random.randn(2, 2)
#    R, S, V = np.linalg.svd(R)
#    if np.linalg.det(R) < 0:
#        u = np.array(R[:, 0])
#        R[:, 0] = R[:, 1]
#        R[:, 1] = u
    theta = -np.pi/4
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    Y = Y.dot(R)

    
    plt.figure(figsize=fSize)
    thetas = np.linspace(0, np.pi/2, 90)
    scores = 0*thetas
    for t in range(len(thetas)):
        theta = thetas[t]
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        XR = (R.dot(X.T)).T
        C = (XR.T).dot(Y)
        scores[t] = C[0, 0] + C[1, 1]
    
    for t in range(len(thetas)):
        plt.clf()
        ax = plt.subplot(121)
        plt.hold(True)
        theta = thetas[t]
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        XR = (R.dot(X.T)).T
        ax.scatter(XR[:, 0], XR[:, 1], 100, 'b')
        ax.scatter(Y[:, 0], Y[:, 1], 100, 'r')
        for i in range(NPoints):
            v = XR[i, :]
            m = np.sqrt(np.sum(v**2))
            v = v*(m-AW)/m
            ax.arrow(0, 0, v[0], v[1], head_width = AW/2, head_length = AW, fc = 'b', ec = 'b')
            v = Y[i, :]
            m = np.sqrt(np.sum(v**2))
            v = v*(m-AW)/m
            ax.arrow(0, 0, v[0], v[1], head_width = AW/2, head_length = AW, fc = 'r', ec = 'r')
            plt.plot([XR[i, 0], Y[i, 0]], [XR[i, 1], Y[i, 1]], 'k')
        
        Z = np.concatenate((X, Y), 0)
        #ax.set_xlim(np.min(Z[:, 0]) - 0.2, np.max(Z[:, 0]) + 0.2)
        ax.set_xlim(-1, 1)
        ax.set_ylim(0, 1.5)
        
        plt.subplot(122)
        plt.plot(scores)
        plt.hold(True)
        plt.stem([t, t], [0, scores[t]])
        #plotPoly2D(A, ax, colors)
        #drawAxes(ax, axRange, axRange)
        plt.savefig('2DProcrustes%i.png'%t, bbox_inches='tight')
    
