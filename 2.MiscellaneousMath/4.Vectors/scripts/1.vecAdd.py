import matplotlib.pyplot as plt
import numpy as np

axO = (0, 0)

# Define the two vectors and their names
vector1 = np.array([2, 3])
vector2 = np.array([-1, 2])


# Calculate the result of vector addition
resultant_vector = vector1 + vector2

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the vectors
ax.quiver(*axO, *vector1, angles='xy', scale_units='xy', scale=1, color='b', label="vec1")
ax.quiver(*axO, *vector2, angles='xy', scale_units='xy', scale=1, color='r', label="vec2")
ax.quiver(*(2,3), *(-1,2), angles='xy', scale_units='xy', scale=1, color='r')

ax.quiver(*axO, *resultant_vector, angles='xy', scale_units='xy', scale=1, color='g', label="vec1+vec2")


# Set the x and y axis limits
ax.set_xlim([-3, 4])
ax.set_ylim([-1, 7])

# Set the labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Vector Addition')

# Add a legend
ax.legend()

# Add text labels for vector names
ax.text(*vector1, "vec1", ha='left', va='bottom')
ax.text(*vector2, "vec2", ha='left', va='bottom')
ax.text(*resultant_vector, "vec1+vec2", ha='left', va='bottom')

# Show the plot
plt.grid()
plt.show()
fig.savefig("vecAdd.png", dpi=150)
