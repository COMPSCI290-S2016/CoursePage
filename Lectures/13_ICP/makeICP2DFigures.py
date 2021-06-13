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

def getCSM(X, Y):
    C = np.sum(X**2, 1)[:, None] + np.sum(Y**2, 1)[None, :] - 2*X.dot(Y.T)
    C[C < 0] = 0
    return np.sqrt(C)

if __name__ == '__main__':
    np.random.seed(100)
    axRange = [-1, 2.2]
    fSize = [12, 6]
    
    NPoints = 30
    t = np.linspace(0, np.pi, NPoints)
    X = np.zeros((NPoints, 2))
    X[:, 0] = np.cos(t)
    X[:, 1] = np.sin(2*t)
    #Apply a little bit of noise and a random rotation and translation
    Y = X + 0.04*np.random.randn(NPoints, 2)
    Y = Y + np.array([5, 5])
    theta = np.pi/4
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    Y = Y.dot(R)
    Y = np.reshape(Y, X.shape)
    Z = np.concatenate((np.array(X), np.array(Y)), 0)
    
    plt.figure(figsize=fSize)
    
    counter = 0
    for i in range(10):
        plt.clf()
        plt.hold(True)
        plt.scatter(X[:, 0], X[:, 1], 30, 'b')
        plt.scatter(Y[:, 0], Y[:, 1], 30, 'r')
        plt.axes().set_aspect('equal', 'datalim')
        plt.xlim([np.min(Z[:, 0]), np.max(Z[:, 0])])
        plt.ylim([np.min(Z[:, 1]), np.max(Z[:, 1])])
        plt.title('Points Iteration %i'%i)
        plt.axis('off')
        plt.savefig('ICPExample/ICP%i_1.svg'%i, bbox_inches='tight')  
        plt.savefig('ICPExample/%i.png'%counter)  
        counter += 1
    
        Y = Y + (np.mean(X, 0) - np.mean(Y, 0))
        if i == 0:
            plt.clf()
            plt.hold(True)
            plt.scatter(X[:, 0], X[:, 1], 30, 'b')
            plt.scatter(Y[:, 0], Y[:, 1], 30, 'r')
            plt.axes().set_aspect('equal', 'datalim')
            plt.xlim([np.min(Z[:, 0]), np.max(Z[:, 0])])
            plt.ylim([np.min(Z[:, 1]), np.max(Z[:, 1])])
            
            plt.title('Mean-Center Iteration %i'%i)
            plt.axis('off')
            plt.savefig('ICPExample/ICP%i_2.svg'%i, bbox_inches='tight')   
            plt.savefig('ICPExample/%i.png'%counter) 
            counter += 1    
    
    
        #First step: find closest points
        plt.clf()
        D = getCSM(X, Y)
        plt.imshow(D)
        idx = np.argmin(D, 0)
        plt.hold(True)
        plt.scatter(np.arange(len(idx)), idx, 20)
        #plt.show()
        XClose = np.array(X[idx, :])
        
        #First plot correspondences
        plt.clf()
        plt.hold(True)
        plt.scatter(X[:, 0], X[:, 1], 30, 'b')
        plt.scatter(Y[:, 0], Y[:, 1], 30, 'r')
        for k in range(NPoints):
            plt.plot([XClose[k, 0], Y[k, 0]], [XClose[k, 1], Y[k, 1]], 'b')
        plt.axes().set_aspect('equal', 'datalim')
        plt.xlim([np.min(Z[:, 0]), np.max(Z[:, 0])])
        plt.ylim([np.min(Z[:, 1]), np.max(Z[:, 1])])
        plt.title('Correspondences Iteration %i'%i)
        plt.axis('off')
        plt.savefig('ICPExample/ICP%i_3.svg'%i, bbox_inches='tight')
        plt.savefig('ICPExample/%i.png'%counter) 
        counter += 1
        
        #Do procrustes on Y
        A = (XClose.T).dot(Y)
        [U, S, VT] = np.linalg.svd(A)
        R = U.dot(VT)
        Y = (R.dot(Y.T)).T
        
        plt.clf()
        plt.hold(True)
        plt.scatter(X[:, 0], X[:, 1], 30, 'b')
        plt.scatter(Y[:, 0], Y[:, 1], 30, 'r')
        for k in range(NPoints):
            plt.plot([XClose[k, 0], Y[k, 0]], [XClose[k, 1], Y[k, 1]], 'b')
        plt.axes().set_aspect('equal', 'datalim')
        plt.xlim([np.min(Z[:, 0]), np.max(Z[:, 0])])
        plt.ylim([np.min(Z[:, 1]), np.max(Z[:, 1])])
        plt.title('Procrustes Iteration %i'%i)
        plt.axis('off')
        plt.savefig('ICPExample/ICP%i_4.svg'%i, bbox_inches='tight')  
        plt.savefig('ICPExample/%i.png'%counter) 
        idx += 1
        
