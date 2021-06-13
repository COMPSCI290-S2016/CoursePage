import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    np.random.seed(100)
    x = np.random.rand(1)*100
    plt.stem([x], [1])
    plt.hold(True)
    y = np.arange(int(np.round(x*2)))
    plt.stem(y, 0*y)
    z = np.exp(-(y-x)**2/10)
    z = z/np.sum(z)
    plt.plot(z, 'r')
    plt.show()
