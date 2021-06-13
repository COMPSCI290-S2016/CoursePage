import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    res = 500
    x = np.linspace(0, 2*np.pi, res)
    [X, Y] = np.meshgrid(x, x)
    wx = 3
    wy = 2
    Z1 = np.cos(wx*X + wy*Y)
    Z2 = np.cos(wx*X - wy*Y)
    Z = Z1 + Z2
    plt.figure(figsize=(12, 4))
    
    plt.subplot(131)
    plt.imshow(Z1)
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(Z2)
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(Z)
    plt.axis('off')
    
    plt.show()
