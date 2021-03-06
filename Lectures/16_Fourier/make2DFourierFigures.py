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

if __name__ == '__main__':
    T1 = 20
    T2 = 15
    NSamples = 60
    t1 = np.linspace(0, 2*np.pi*NSamples/T1, NSamples)
    t2 = np.linspace(0, 2*np.pi*NSamples/T2, NSamples)
    s1 = np.cos(t1)
    s2 = np.cos(t2)
    
    #Cos^2 Example
    plt.figure(figsize=(10, 6))
    plt.subplot(211)
    plotPosNeg(s1)
    plt.title('cos(2pi/20 t)')
    plt.axis('off')
    s1Sqr = s1**2
    plt.subplot(212)
    plotPosNeg(s1Sqr)
    plt.title('cos(2pi/20 t)*cos(2pi/20 t)')
    plt.axis('off')
    plt.ylim(-1, 1)
    plt.savefig("cosSqr.svg", bbox_inches = 'tight')
    
    #cossine Example
    s3 = np.sin(t1)
    plt.figure(figsize=(12, 8))
    plt.subplot(311)
    plotPosNeg(s1)
    plt.title('cos(2pi/20 t)')
    plt.axis('off')
    
    plt.subplot(312)
    plotPosNeg(s3)
    plt.title('sin(2pi/20 t)')
    plt.axis('off')
    
    s1Prod = s1*s3
    plt.subplot(313)
    plotPosNeg(s1Prod)
    plt.title('cos(2pi/20 t)*sin(2pi/20 t)')
    plt.axis('off')
    plt.savefig("cossin.svg", bbox_inches = 'tight')
    
    #CosACosB example
    NSamples = 120
    t1 = np.linspace(0, 2*np.pi*NSamples/T1, NSamples)
    t2 = np.linspace(0, 2*np.pi*NSamples/T2, NSamples)
    s1 = np.cos(t1)
    s2 = np.cos(t2)
    plt.figure(figsize=(12, 8))
    plt.subplot(311)
    plotPosNeg(s1)
    plt.title('cos(2pi/20 t)')
    plt.axis('off')
    
    plt.subplot(312)
    plotPosNeg(s2)
    plt.title('cos(2pi/15 t)')
    plt.axis('off')
    
    s1Prod = s1*s2
    plt.subplot(313)
    plotPosNeg(s1Prod)
    plt.title('cos(2pi/20 t)*cos(2pi/15 t)')
    plt.axis('off')
    plt.savefig("cosProd1.svg", bbox_inches = 'tight')
    
    #cosA(cosA+cosB) example
    s1 = s1 + s2
    plt.figure(figsize=(12, 8))
    plt.subplot(311)
    plotPosNeg(s1)
    plt.title('cos(2pi/20 t) + cos(2pi/15 t)')
    plt.axis('off')
    
    plt.subplot(312)
    plotPosNeg(s2)
    plt.title('cos(2pi/15 t)')
    plt.axis('off')
    
    s1Prod = s1*s2
    plt.subplot(313)
    plotPosNeg(s1Prod)
    plt.title('cos(2pi/15 t) * (cos(2pi/20 t) + cos(2pi/15 t))')
    plt.axis('off')
    plt.savefig("cosProd2.svg", bbox_inches = 'tight')
    
    #Phase Example
    NSamples = 60
    t1 = np.linspace(0, 2*np.pi*NSamples/T1, NSamples)
    t2 = np.linspace(0, 2*np.pi*NSamples/T2, NSamples)
    s1 = np.cos(t1)
    s2 = np.cos(t2)
    
    #Cos^2 Example
    plt.figure(figsize=(10, 6))
    plt.subplot(211)
    plotPosNeg(s1)
    plt.title('cos(2pi/20 t)')
    plt.axis('off')
    s1Sqr = s1**2
    plt.subplot(212)
    plotPosNeg(s1Sqr)
    plt.title('cos(2pi/20 t)*cos(2pi/20 t)')
    plt.axis('off')
    plt.ylim(-1, 1)
    plt.savefig("cosSqr.svg", bbox_inches = 'tight')
