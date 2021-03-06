import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 1000
    t = np.linspace(0, 2*np.pi, N)
    x = np.cos(t)
    y = np.sin(t)
    cmap = plt.get_cmap('jet')
    i = 1
    for k in range(8):
        fc = (1+np.cos(t*k))/2
        fs = (1+np.sin(t*k))/2
        C = cmap(fc)[:, 0:3]
        plt.subplot(4, 4, i)
        plt.scatter(x, y, 20, C, edgecolors = 'none')
        plt.axis('off')
        i += 1
        C = cmap(fs)[:, 0:3]
        plt.subplot(4, 4, i)
        plt.scatter(x, y, 20, C, edgecolors = 'none')
        plt.axis('off')
        i += 1
    plt.show()
