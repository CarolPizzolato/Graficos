import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np

alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def ColorMap(phi_m, phi_p):
    return (+alpha - 2 * np.cos(phi_m) - alpha * np.cos(phi_ext - 2 * phi_p))

phi_m = np.linspace(0, 2 * np.pi, 100)
phi_p = np.linspace(0, 2 * np.pi, 100)

x, y = np.meshgrid(phi_p, phi_m)
z = ColorMap(y, x)  # ou: z = ColorMap(*np.meshgrid(phi_m, phi_p))[0]

fig = plt.figure(figsize=(14, 6))

ax = fig.add_subplot(1, 2, 1, projection='3d')
p = ax.plot_surface(x, y, z, rstride=4, cstride=4, linewidth=0)

ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

cb = fig.colorbar(p, shrink=0.5)
plt.show()
