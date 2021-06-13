import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

if __name__ == '__main__':
    N = 200
    step = 10
    NPulses = 3

    #Step 1: Generate a random 1D function
    np.random.seed(9)
    x = np.arange(0, N, step)
    y = np.random.randn(x.size)
    s = UnivariateSpline(x, y, s=1)
    xs = np.arange(N)
    y = s(xs)
    
    
    #Step 2: Generate a random set of impulses
    PIdx = np.random.permutation(N)[0:2*NPulses]
    idx = np.argsort(PIdx)
    PIdx = np.sort(PIdx)
    PMag = np.zeros(2*NPulses)
    PMag[0:NPulses] = -np.abs(np.random.randn(NPulses))
    PMag[NPulses:] = np.abs(np.random.randn(NPulses))
    PMag = PMag[idx]
    
    
    #Step 3: Plot Original function and impulse response
    
    #Step 4: Plot adding one impulse at a time
    R = np.max(np.abs(y))*np.max(np.abs(PMag))
    out = np.zeros(2*N)
    for p in range(len(PMag)):
        out[PIdx[p]:PIdx[p]+N] += PMag[p]*y
        plt.figure(figsize=[16, 10])
        plt.subplot(311)
        plt.plot(y)
        plt.xlim(0, 2*N)
        plt.ylim(-R, R)
        plt.xlabel('Sample Number')
        plt.ylabel('Amplitude')
        plt.title('Original Function')
        
        plt.subplot(312)
        plt.stem(PIdx, PMag, 'k')
        plt.hold(True)
        plt.plot([PIdx[p], PIdx[p]], [-R, R])
        plt.xlim(0, 2*N)
        plt.ylim(-R, R)
        plt.ylabel('Amplitude')
        plt.xlabel('Sample Number')
        
        plt.subplot(313)
        plt.hold(True)
        x = np.arange(len(y))
        for i in range(p+1):
            if (i == p):
                plt.plot(x+PIdx[i], y*PMag[i], 'b', linewidth=4.0)
            else:
                plt.plot(x+PIdx[i], y*PMag[i], 'k', linewidth=1.0)
        plt.plot([PIdx[p], PIdx[p]], [-R, R])
        plt.xlim(0, 2*N)
        plt.ylim(-R, R)
        plt.ylabel('Amplitude')
        plt.xlabel('Sample Number')
        
        plt.savefig("Conv%i.svg"%p, bbox_inches='tight')
        
    #Now plot the result
    plt.figure(figsize=[16, 10])
    plt.subplot(311)
    plt.plot(y)
    plt.xlim(0, 2*N)
    plt.ylim(-R, R)
    plt.xlabel('Sample Number')
    plt.ylabel('Amplitude')
    plt.title('Original Function')
    
    plt.subplot(312)
    plt.stem(PIdx, PMag, 'k')
    plt.xlim(0, 2*N)
    plt.ylim(-R, R)
    plt.ylabel('Amplitude')
    plt.xlabel('Sample Number')
    
    plt.subplot(313)
    plt.plot(out)
    plt.ylabel('Amplitude')
    plt.xlabel('Sample Number')
    plt.savefig("ConvResult.svg", bbox_inches='tight')

    #Convolution ground truth    
#    plt.figure()
#    P = np.zeros(2*N)
#    P[PIdx] = PMag
#    plt.plot(np.convolve(y, P))
#    plt.show()

