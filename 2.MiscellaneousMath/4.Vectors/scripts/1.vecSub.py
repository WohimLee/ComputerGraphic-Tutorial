

import numpy as np
import matplotlib.pyplot as plt

AxO = (0, 0)

vec1 = np.array([1, 2])
vec2 = np.array([-3, 2])


fig, ax = plt.subplots()

ax.quiver(*AxO, *vec1, angles='xy', scale_units='xy', scale=1, color='r', label='vec1')
ax.quiver(*AxO, *vec2, angles='xy', scale_units='xy', scale=1, color='b', label='vec2')
ax.quiver(*AxO, *(-vec1), angles='xy', scale_units='xy', scale=1, color='g', label='-vec1')

ax.set_xlim([-5, 2])
ax.set_ylim([-3, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

plt.grid()
plt.show()
