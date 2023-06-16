
import numpy as np
import matplotlib.pyplot as plt

O = (0,0)

vec = np.array([2, 3])
scale = np.array([
    [0.5, 0],
    [0, 0.5]
])

res = scale @ vec

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

ax1 = axes[0]
ax1.quiver(*O, *vec, angles='xy', scale_units='xy' ,scale=1, color='r')
ax1.set_xlim([-1, 3])
ax1.set_ylim([-1, 3])
ax1.grid()

ax2 = axes[1]
ax2.quiver(*O, *res, angles='xy', scale_units='xy', scale=1, color='r')
ax2.set_xlim([-1, 3])
ax2.set_ylim([-1, 3])
ax2.grid()

plt.show()