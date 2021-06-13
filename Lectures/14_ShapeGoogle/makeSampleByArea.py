import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    X = np.random.rand(1000, 2)
    plt.plot(X[:, 0], X[:, 1], '.')
    plt.axis('off')
    plt.show()
