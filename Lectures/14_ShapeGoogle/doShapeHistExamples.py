import numpy as np
import matplotlib.pyplot as plt

NCIRC = 100

def getDisc(N):
#    [I, J] = np.meshgrid(np.linspace(0, 2*np.pi, N), np.linspace(0, 1.0, N))
#    I = I.flatten()
#    J = J.flatten()
#    X = np.zeros((N*N, 2))
#    X[:, 0] = J*np.cos(I)
#    X[:, 1] = J*np.sin(I)
    R = np.random.rand(N)
    R = R/(0.5 + R)
    theta = np.random.rand(N)*2*np.pi
    X = np.zeros((N, 2))
    X[:, 0] = R*np.cos(theta)
    X[:, 1] = R*np.sin(theta)
    return X
    
def getRot(theta):
    [C, S] = [np.cos(theta), np.sin(theta)]
    Rot = np.array([[C, -S], [S, C]])    
    return Rot

if __name__ == '__main__':
    np.random.seed(100)
    

    #Torso
    X1 = getDisc(1000)
    X1[:, 1] = X1[:, 1]*5
    
    #Head
    X2 = 2*getDisc(400)
    X2 = X2 + np.array([[0, 5]])
    
    #Arms
    X = np.array([0.5, 5])*getDisc(400)
    Rot = getRot(np.pi/4)
    X3 = X.dot(Rot) - np.array([[2.2, -1]]) #Left Arm
    X4 = X.dot(Rot.T) + np.array([[2.2, 1]]) #Right Arm
    
    X5 = X.dot(Rot) - np.array([[2.2, 5]]) #Left Leg
    X6 = X.dot(Rot.T) + np.array([[2.2, -5]]) #Right Leg
    
    X = np.concatenate((X1, X2, X3, X4, X5, X6), 0)
    X = X - np.mean(X, 0) #Center on centroid
    R = np.sqrt(np.sum(X**2, 1))
    Rs = np.linspace(0, np.max(R), 10) #Compute radii of all points
    
    #First plot person point cloud
    plt.plot(X[:, 0], X[:, 1], '.')
    plt.xlim(np.min(X[:, 0]), np.max(X[:, 0]))
    plt.ylim(np.min(X[:, 1]), np.max(X[:, 1]))
    plt.axes().set_aspect('equal', 'datalim')
    plt.axis('off')
    plt.savefig("Person.svg", bbox_inches='tight')
    
    #Now compute and plot shell histogram
    hist = np.zeros(len(Rs))
    
#    for i in range(1, len(Rs)):
#        plt.clf()
#        plt.figure(figsize = (12, 6))
#        plt.subplot(121)
#        plt.plot(X[:, 0], X[:, 1], '.')
#        plt.hold(True)
#        t = np.linspace(0, 2*np.pi, NCIRC)
#        for k in range(0, len(Rs)):
#            C = np.zeros((NCIRC, 2))
#            C[:, 0] = Rs[k]*np.cos(t)
#            C[:, 1] = Rs[k]*np.sin(t)
#            if (k == i or k == i-1):
#                plt.plot(C[:, 0], C[:, 1], 'r')
#            else:
#                plt.plot(C[:, 0], C[:, 1], 'k')
#        #Now figure out which points are in the shell
#        idx = np.zeros(len(R))
#        idx[R < Rs[i]] = 1
#        idx[R < Rs[i-1]] = 0
#        hist[i-1] = np.sum(idx)
#        Y = X[idx == 1, :]
#        plt.plot(Y[:, 0], Y[:, 1], '.', color="red")
#        plt.xlim(np.min(X[:, 0]), np.max(X[:, 0]))
#        plt.ylim(np.min(X[:, 1]), np.max(X[:, 1]))
#        plt.axis('off')
#        #plt.axes().set_aspect('equal', 'datalim')
#        plt.subplot(122)
#        plt.title('Shape Histogram')
#        plt.bar(np.arange(hist.size), hist)
#        plt.hold(True)
#        plt.bar([i-1], [hist[i-1]], color = "r")
#        plt.ylim([0, 800])
#        plt.savefig("ShapeHist%i.svg"%i, bbox_inches='tight')
    
    #Plot what happens rotating one of the shells
#    thetas = np.linspace(0, np.pi/4, 50)
#    for i in range(len(thetas)):
#        plt.clf()
#        Z = np.array(X)
#        
#        Rot = getRot(thetas[i])
#        idx = np.arange(Z.shape[0])
#        idx[R > Rs[3]] = -1
#        idx[R < Rs[2]] = -1
#        idx = idx[idx >= 0]
#        Z[idx, :] = Z[idx, :].dot(Rot)
#        
#        plt.plot(Z[:, 0], Z[:, 1], '.')
#        plt.hold(True)
#        t = np.linspace(0, 2*np.pi, NCIRC)
#        for k in range(0, len(Rs)):
#            C = np.zeros((NCIRC, 2))
#            C[:, 0] = Rs[k]*np.cos(t)
#            C[:, 1] = Rs[k]*np.sin(t)
#            plt.plot(C[:, 0], C[:, 1], 'b')       
#        plt.xlim(np.min(X[:, 0]), np.max(X[:, 0]))
#        plt.ylim(np.min(X[:, 1]), np.max(X[:, 1]))
#        plt.axes().set_aspect('equal', 'datalim')
#        plt.axis('off')
#        plt.savefig("HistRot%i.png"%i)
#        if i == len(thetas)-1:
#            X = Z
#    thetas = np.linspace(0, np.pi/4, 50)
#    for i in range(len(thetas)):
#        plt.clf()
#        Z = np.array(X)
#        
#        Rot = getRot(thetas[i])
#        idx = np.arange(Z.shape[0])
#        idx[R > Rs[5]] = -1
#        idx[R < Rs[4]] = -1
#        idx = idx[idx >= 0]
#        Z[idx, :] = Z[idx, :].dot(Rot)
#        
#        plt.plot(Z[:, 0], Z[:, 1], '.')
#        plt.hold(True)
#        t = np.linspace(0, 2*np.pi, NCIRC)
#        for k in range(0, len(Rs)):
#            C = np.zeros((NCIRC, 2))
#            C[:, 0] = Rs[k]*np.cos(t)
#            C[:, 1] = Rs[k]*np.sin(t)
#            plt.plot(C[:, 0], C[:, 1], 'b')
#        plt.xlim(np.min(X[:, 0]), np.max(X[:, 0]))
#        plt.ylim(np.min(X[:, 1]), np.max(X[:, 1]))
#        plt.axes().set_aspect('equal', 'datalim')
#        plt.axis('off')
#        plt.savefig("HistRot%i.png"%(i+len(thetas)))

    #Do shells and sectors
    PThetas = np.mod(2*np.pi + np.arctan2(X[:, 1], X[:, 0]), 2*np.pi)
    thetas = np.linspace(0, 2*np.pi, 10)
    hist = np.zeros(len(thetas-1)*len(Rs-1))
    binnum = 0
    for i in range(1, len(Rs)):
        for j in range(1, len(thetas)):
            plt.clf()
            plt.figure(figsize = (12, 6))
            plt.subplot(121)
            plt.plot(X[:, 0], X[:, 1], '.')
            plt.hold(True)
            t = np.linspace(0, 2*np.pi, NCIRC)
            for k in range(0, len(Rs)):
                C = np.zeros((NCIRC, 2))
                C[:, 0] = Rs[k]*np.cos(t)
                C[:, 1] = Rs[k]*np.sin(t)
                plt.plot(C[:, 0], C[:, 1], 'k')
                if k == i or k == i-1:
                    idx = np.ones(NCIRC)
                    idx[t < thetas[j-1]] = 0
                    idx[t > thetas[j]] = 0
                    plt.plot(C[idx == 1, 0], C[idx == 1, 1], 'r', linewidth=3.0)
            for k in range(0, len(thetas)):
                C = [np.max(Rs)*np.cos(thetas[k]), np.max(Rs)*np.sin(thetas[k])]
                plt.plot([0, C[0]], [0, C[1]], 'b')
                if k == j or k == j-1:
                    Cx = Rs[i-1:i+1]*np.cos(thetas[k])
                    Cy = Rs[i-1:i+1]*np.sin(thetas[k])
                    plt.plot(Cx, Cy, 'r', linewidth=3.0)
            #Now figure out which points are in the shell
            idx = np.zeros(len(R))
            idx[R < Rs[i]] = 1
            idx[R < Rs[i-1]] = 0
            idx[PThetas < thetas[j-1]] = 0
            idx[PThetas > thetas[j]] = 0
            hist[binnum] = np.sum(idx)
            Y = X[idx == 1, :]
            plt.plot(Y[:, 0], Y[:, 1], '.', color="red")
            plt.xlim(np.min(X[:, 0]), np.max(X[:, 0]))
            plt.ylim(np.min(X[:, 1]), np.max(X[:, 1]))
            plt.axis('off')
            #plt.axes().set_aspect('equal', 'datalim')
            plt.subplot(122)
            plt.title('Shape Shell/Sector Histogram')
            plt.bar(np.arange(hist.size), hist)
            plt.hold(True)
            plt.bar([binnum], [hist[binnum]], color = "r")
            plt.ylim([0, 300])
            plt.savefig("ShapeHistSectors%i.png"%binnum, bbox_inches='tight')
            binnum += 1
            plt.close("all")
