import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    np.random.seed(14)
    X = np.random.rand(100, 2)
    GridLim = 10
    grid = np.linspace(0, 1, GridLim)
    dx = grid[1]-grid[0]
    idx = np.array(np.floor(X/dx), dtype=np.int64)
    D = np.zeros((GridLim, GridLim))
    for i in range(idx.shape[0]):
        D[idx[i, 0], idx[i, 1]] += 1
    plt.imshow(D, interpolation='none', aspect='auto', cmap=plt.get_cmap('Greys'), origin = 'lower')
    plt.hold(True)
    plt.plot(GridLim*X[:, 0], GridLim*X[:, 1], '.', color='red')
    plt.colorbar()
    plt.show()
