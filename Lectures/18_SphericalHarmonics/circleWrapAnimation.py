import numpy as np
import matplotlib.pyplot as plt

def plotPosNeg(s):
    idxn = np.arange(len(s))
    sn = s[s < 0]
    idxn = idxn[s < 0]
    sp = s[s >= 0]
    idxp = np.arange(len(s))
    idxp = idxp[s >= 0]
    if len(idxp) > 0:
        plt.stem(idxp, sp, 'r', markerfmt='ro')
        plt.hold(True)
    if len(idxn) > 0:
        plt.stem(idxn, sn, 'b')

if __name__ == '__main__2':
    N = 31
    for i in range(N):
        f = np.floor((i+1)/2)
        print(f)
        plt.subplot(6, 6, i)
        y = np.cos(np.arange(N)*2*np.pi*f/N)
        if i%2 == 0:
            y = np.sin(np.arange(N)*2*np.pi*f/N)
        plt.plot(y)
        plt.axis('off')
    plt.show()

if __name__ == '__main__':
    N = 401
    t = np.arange(N)
    x = 2.5*np.exp(-(t-80.0)**2/(7.0**2))
    x += 2.5*np.exp(-(t-160.0)**2/(7**2))
    x += 0.5*np.exp(-(t-120.0)**2/(10.0**2))
    x += 2*np.exp(-(t-(N-120.0))**2/(10.0**2))
    x += 2*np.exp(-(t-(N-60.0))**2/(10.0**2))
    
    Rs = 1.2**(np.linspace(0, 20, 300.0))
    Rs = np.fliplr(Rs[None, :]).flatten()
    plt.figure(figsize=(11.0/4, 7.0/4))
    
    for i in range(len(Rs)):
        R = Rs[i]
 
        tc = np.linspace(np.pi/2-np.pi/R, np.pi/2 + np.pi/R, N)
        X = np.zeros((N, 2))
        X[:, 0] = (R + x)*np.cos(tc)
        X[:, 1] = (R + x)*np.sin(tc)
        Y = np.zeros((N, 2))
        Y[:, 0] = R*np.cos(tc)
        Y[:, 1] = R*np.sin(tc)
        Y = Y - X[0, :]
        X = X - X[0, :]
        
        plt.clf()
        plt.plot(Y[:, 0], Y[:, 1], 'b', lineWidth=2)
        plt.hold(True)
        plt.plot(X[:, 0], X[:, 1], 'r', lineWidth=2)
        plt.axis('equal')
        plt.xlim([-7, 4])
        plt.ylim([-2, 5])
        plt.axis('off')
        plt.savefig("CircleWrap%i.png"%i, dpi = 120, bbox_inches='tight')

