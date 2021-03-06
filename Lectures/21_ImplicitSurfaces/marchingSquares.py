import numpy as np
import matplotlib.pyplot as plt

from skimage import measure


# Construct some test data
g = np.linspace(0, 2*np.pi, 100)
x, y = np.meshgrid(g, g)
r = np.cos(2*x + 4*y) + np.cos(2*x - 4*y)

# Find contours at a constant value of 0.8
contours = measure.find_contours(r, 0.5)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(r, interpolation='nearest', cmap=plt.cm.gray)
plt.axis('off')
plt.savefig("EggCartonImg.png", dpi = 200, bbox_inches = 'tight')

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], 'r')


plt.savefig("EggCartonImpContours.png", dpi=200, bbox_inches = 'tight')
