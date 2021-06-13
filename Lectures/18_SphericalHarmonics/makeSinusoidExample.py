import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    A = 10
    omega = 1
    phi = 1
    
    t = np.linspace(0, 2*np.pi, 1000)
    y = A*np.cos(t*omega + phi)
    
    y1 = A*np.cos(phi)*np.cos(t*omega)
    y2 = -A*np.sin(phi)*np.sin(t*omega)
    
    z = y1 + y2
    
    plt.figure(figsize=(12, 6))
    plt.plot(t, z, 'k')
    plt.savefig("SineDecomp1.svg", bbox_inches='tight')
    plt.hold(True)
    plt.plot(t, y1, 'r')
    plt.savefig("SineDecomp2.svg", bbox_inches='tight')
    plt.plot(t, y2, 'b')
    plt.savefig("SineDecomp3.svg", bbox_inches='tight')
    
    plt.show()
