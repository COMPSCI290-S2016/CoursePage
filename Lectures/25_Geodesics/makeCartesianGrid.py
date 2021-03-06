import numpy as np
import matplotlib.pyplot as plt

def plotGrid(res):
    g = np.arange(res)
    [I, J] = np.meshgrid(g, g)
    plt.scatter(I.flatten(), J.flatten(), 20)
    plt.hold(True)
    for i in range(len(g)):
        plt.plot([g[0], g[-1]], [g[i], g[i]], 'k')
        plt.plot([g[i], g[i]], [g[0], g[-1]], 'k')
    plt.axis('off')
    return g

if __name__ == '__main__':
#    plotGrid(8)
#    plt.savefig("8x8Cartesian.svg", bbox_inches='tight')
    plt.clf()
    plotGrid(15)
    plt.savefig("15x15Cartesian.svg", bbox_inches='tight')
