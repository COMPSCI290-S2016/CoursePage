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
    N = 301
    #x = np.exp(-(np.array(np.arange(N), dtype=np.int64)-150.0)**2/(10.0**2))
    for shift in range(1, 250):
        x = np.arange(N)/float(N)
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
        
        plt.clf()
        plt.figure(figsize=(10, 6))
        plt.subplot(221)
        plt.plot(z, 'b')
        plt.hold(True)
        z[0:N] = 0
        z[-N:] = 0
        plt.plot(z, 'r')
        plt.plot([N, N], [0, 1.0], 'r')
        plt.plot([2*N, 2*N], [0, 1.0], 'r')
        plt.title('Signal')
        plt.subplot(223)
        plt.stem(np.array(cosines)[0:15])
        plt.ylim([-30, 30])
        plt.title('Cosines')
        plt.subplot(224)
        plt.stem(np.array(sines)[0:15])
        plt.ylim([-30, 30])
        plt.title('Sines')
        plt.subplot(222)
        mags = np.sqrt(np.array(sines)**2 + np.array(cosines)**2)
        plt.stem(mags[0:15])
        plt.title('Magnitudes')
        plt.savefig("Ramp%i.png"%shift, dpi = 120, bbox_inches='tight')

