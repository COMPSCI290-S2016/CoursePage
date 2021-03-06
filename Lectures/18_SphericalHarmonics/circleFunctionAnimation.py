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
    N = 360
    #x = np.exp(-(np.array(np.arange(N), dtype=np.int64)-150.0)**2/(10.0**2))
    plt.figure(figsize=(7, 3))
    for shift in range(1, N):
        t = np.arange(N)
        x = 2.5*np.exp(-(t-80.0)**2/(7.0**2))
        x += 2.5*np.exp(-(t-160.0)**2/(7**2))
        x += 0.5*np.exp(-(t-120.0)**2/(10.0**2))
        x += 2*np.exp(-(t-(N-120.0))**2/(10.0**2))
        x += 2*np.exp(-(t-(N-60.0))**2/(10.0**2))
        if shift == 1:
            plt.plot(x)
            plt.savefig('5Gaussians.svg', bbox_inches='tight')
        y = 0*x
        y[0:shift] = x[-shift:]
        y[shift:] = x[0:-shift]
        x = y
        basis = []
        coeffs = []
        zgt = 0*x
        sines = []
        cosines = []
        strings = []
        for i in range(N):
            f = np.floor((i+1)/2)
            y = np.cos(np.arange(N)*2*np.pi*f/N)
            if i%2 == 1:
                y = np.sin(np.arange(N)*2*np.pi*f/N)
            basis.append(y)
            coeffs.append(np.sum(y*x))
            zgt += coeffs[i]*basis[i]/(float(N/2))
            if i == 0:
                strings.append('DC')
                continue
            if i%2 == 1:
                sines.append(coeffs[i])
                strings.append('Sine %i'%f)
            else:
                cosines.append(coeffs[i])
                strings.append('Cosine %i'%f)
        
        z = np.concatenate((x[None, :], x[None, :], x[None, :]), 1).flatten()
        tc = np.linspace(0, 2*np.pi, N)
        X = np.zeros((N, 2))
        X[:, 0] = (1 + x)*np.cos(tc)
        X[:, 1] = (1 + x)*np.sin(tc)
        X = np.concatenate((X, X[0, :][None, :]), 0) #Close loop
        
        plt.clf()
        plt.subplot(121)
        plt.plot(x, 'r', lineWidth=2)
        plt.xlabel("Degrees")
        ax = plt.gca()
        ax.set_yticks([])
        plt.title('Signal')
        plt.subplot(122)
        plt.plot(X[:, 0], X[:, 1], 'r', lineWidth=4)
        M = (np.max(np.abs(x)) + 1.5)*np.sqrt(2)
        plt.axis('equal')
        plt.xlim([-M, M])
        plt.ylim([-M, M])
        ax = plt.gca()
        ax.set_xticks([])
        ax.set_yticks([])
        plt.title('Wrapped Around Circle')
        plt.savefig("CircleShift%i.png"%shift, dpi = 120, bbox_inches='tight')

