import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_camera_pose(camera_pose):
    # Define the camera center
    camera_center = camera_pose[:3, 3]

    # Extract the camera rotation matrix
    camera_rotation = camera_pose[:3, :3]

    # Define the coordinate axes
    axes_length = 0.5
    axes = axes_length * np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # Transform the coordinate axes based on the camera rotation
    transformed_axes = np.dot(camera_rotation, axes.T).T

    # Create a new figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the camera center
    ax.scatter(*camera_center, c='r', marker='o', label='Camera Center')

    # Plot the coordinate axes
    ax.quiver(*camera_center,
              transformed_axes[:, 0], transformed_axes[:, 1], transformed_axes[:, 2],
              color=['r', 'g', 'b'], length=axes_length)

    # Set plot limits
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()

# Example camera pose (translation of (1, 1, 1) and rotation of 45 degrees around Y-axis)
camera_pose = np.array([[np.cos(np.pi/4), 0, np.sin(np.pi/4), 1],
                        [0, 1, 0, 1],
                        [-np.sin(np.pi/4), 0, np.cos(np.pi/4), 1],
                        [0, 0, 0, 1]])
print(camera_pose)
# Call the function to plot the camera pose
plot_camera_pose(camera_pose)
