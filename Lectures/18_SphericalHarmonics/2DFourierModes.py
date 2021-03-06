import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    res = 500
    x = np.linspace(0, 2*np.pi, res)
    [X, Y] = np.meshgrid(x, x)
    wx = 1
    wy = 0
    Z = np.cos(wx*X + wy*Y)
    plt.imshow(Z)
    plt.hold(True)
    plt.scatter([res/10.0*wx], [res/10.0*wy], 50, 'k')
    plt.arrow(res/10.0*wx, res/10.0*wy, res/3.0*wx, res/3.0*wy, head_width = res/20, head_length = res/20, fc = 'k', ec = 'k')
    plt.axis('off')
    plt.show()
