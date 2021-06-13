import sys

import numpy as np
import matplotlib.pyplot as plt
import mcubes #https://github.com/pmneila/PyMCubes

def saveOffFileExternal(filename, VPos, ITris):
    #Save off file given buffers, not necessarily in the PolyMesh object
    nV = VPos.shape[0]
    nF = ITris.shape[0]
    fout = open(filename, "w")
    fout.write("OFF\n%i %i %i\n"%(nV, nF, 0))
    for i in range(nV):
        fout.write("%g %g %g\n"%tuple(VPos[i, :]))
    for i in range(nF):
        fout.write("3 %i %i %i\n"%tuple(ITris[i, :]))
    fout.close()

if __name__ == '__main__':
    X, Y, Z = np.mgrid[:100, :100, :100]
    u = np.exp(-((X-70.0)**2 + (Y-70.0)**2 + (Z-70.0)**2)/(2.0*5.0**2))
    u += np.exp(-((X-50.0)**2 + (Y-50.0)**2 + (Z-50.0)**2)/(2.0*15.0**2))
    u = u - 0.2
    VPos, ITris = mcubes.marching_cubes(u, 0)
    saveOffFileExternal("out.off", VPos, ITris)
