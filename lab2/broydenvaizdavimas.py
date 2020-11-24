import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

X = np.arange(-10, 10, 0.01)
Y = np.arange(-10, 10, 0.01)
XX, YY = np.meshgrid(X, Y)

Z1 = (XX**2)/4 + (YY**2)/2 - 4
Z2 = 10 * np.sin(XX) * np.cos(YY/2)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XX, YY, Z1, cmap=cm.coolwarm, alpha=0.5)
surfZ = ax.plot_surface(XX, YY, np.zeros(np.shape(Z1)), antialiased=False, alpha=0.2)
cp = ax.contour(X, Y, Z1, levels=0, colors='red')
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XX, YY, Z2, cmap=cm.summer, antialiased=False, alpha=0.5)
surfZ = ax.plot_surface(XX, YY, np.zeros(np.shape(Z1)), antialiased=False, alpha=0.2)
cp = ax.contour(X, Y, Z2, levels=0, colors='green')
plt.show()

fig = plt.figure()
ax = fig.gca()
ax.grid(color='#C0C0C0', linestyle='-', linewidth=0.5)
cp = ax.contour(X, Y, Z1, levels=0, colors='red')
cp = ax.contour(X, Y, Z2, levels=0, colors='green')
plt.show()
