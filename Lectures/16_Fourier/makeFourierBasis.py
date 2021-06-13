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
        print f
        plt.subplot(6, 6, i)
        y = np.cos(np.arange(N)*2*np.pi*f/N)
        if i%2 == 0:
            y = np.sin(np.arange(N)*2*np.pi*f/N)
        plt.plot(y)
        plt.axis('off')
    plt.show()

if __name__ == '__main__':
    N = 31
    x = 1.0*np.arange(N)
    x = np.exp(-(np.array(np.arange(N), dtype=np.int64)-15.0)**2/(5.0**2))
    #x = np.arange(N)
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
    
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.subplot(311)
    plt.stem(x)
    plt.title('Signal')
    plt.subplot(312)
    plt.stem(np.array(cosines))
    plt.ylim([-8, 8])
    plt.title('Cosines')
    plt.subplot(313)
    plt.stem(np.array(sines))
    plt.ylim([-8, 8])
    plt.subplot(313)
    plt.title('Sines')
    plt.savefig("SignalDecomposition.svg", bbox_inches='tight')
    
    plt.clf()
    plt.figure(figsize=(8, 8))
    z = 0*x
    for i in range(N):
        z += coeffs[i]*basis[i] / float(N/2)
        plt.clf()
        plt.plot(z)
        plt.hold(True)
        plt.plot(zgt, 'r')
        plt.ylim([-np.max(zgt)/4, np.max(zgt)])
        plt.axis('off')
        plt.title(strings[i])
        plt.savefig("%i.png"%i, bbox_inches = 'tight')
