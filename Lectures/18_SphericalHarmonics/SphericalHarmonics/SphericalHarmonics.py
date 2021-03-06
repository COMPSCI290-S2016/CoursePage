#Programmer: Chris Tralie
#Purpose: Code to generate spherical harmonic meshes
import sys
sys.path.append("S3DGLPy")
from Primitives3D import *
from PolyMesh import *
from scipy.special import sph_harm

import scipy.sparse
import scipy.stats
import scipy.sparse.linalg as slinalg
import numpy as np
import matplotlib.pyplot as plt

#Put spherical harmonics onto the sphere mesh.  Assumes a unit sphere
def getSphericalHarmonics(m, pl, pm, reim = True, updatePos = True):
    cmap = plt.get_cmap('jet')
    cosphi = m.VPos[:, 2]
    sinphi = np.sqrt(1-cosphi**2)
    costheta = m.VPos[:, 0]/sinphi
    sintheta = m.VPos[:, 1]/sinphi
    costheta[sinphi == 0] = 1
    sintheta[sinphi == 0] = 1
    cosphi[cosphi < -1] = -1
    cosphi[cosphi > 1] = 1
    costheta[costheta < -1] = -1
    costheta[costheta > 1] = 1
    phi = np.arccos(cosphi)
    theta = np.arccos(costheta)
    Y = sph_harm(pl, pm, theta, phi)
    if reim:
        Y = np.real(Y)
    else:
        Y = np.imag(Y)
    if updatePos:
        m.VPos = m.VPos*Y[:, None]
    Y = Y - np.min(Y)
    Y = Y/np.max(Y)
    m.VColors = np.array(np.round(255.0*cmap(Y)[:, 0:3]), dtype=np.int64)


if __name__ == '__main__':
    import scipy.io as sio
    mesh = getSphereMesh(1, 4)
    mesh.updateTris()
    mesh.saveOffFile("out.off")
    sio.savemat("Sphere.mat", {"VPos":mesh.VPos, "ITris":mesh.ITris})

if __name__ == '__main__2':
    for l in range(5):
        for m in range(l+1):
            mesh = getSphereMesh(1, 5)
            getSphericalHarmonics(mesh, m, l)
            mesh.saveOffFile("SphHarm_%i_%i_Real.off"%(l, m), output255 = True)
            mesh = getSphereMesh(1, 5)
            getSphericalHarmonics(mesh, m, l, updatePos = False)
            mesh.saveOffFile("SphHarm_%i_%i_Real_ColorsOnly.off"%(l, m), output255 = True)
