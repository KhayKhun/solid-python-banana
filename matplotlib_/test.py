import numpy as np
import matplotlib.pyplot as plt

# Load the points data (assuming two columns: x and y coordinates)
points = np.loadtxt("points.csv", delimiter=",")  # Adjust filename if needed

# Load the distances data (assuming a single column with distance values)
distances = np.loadtxt("distances.csv", delimiter=",")  

# Ensure both arrays have the correct shape
if points.shape[0] != distances.shape[0]:
    raise ValueError("The number of points and distances must be the same.")

# Create a scatter plot with color mapping
plt.figure(figsize=(8, 6))
sc = plt.scatter(points[:, 0], points[:, 1], c=distances, cmap="viridis", edgecolors='black')

# Add color bar to show the scale of distances
plt.colorbar(sc, label="Distance Value")

# Labels and title
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Scatter Plot of Points Colored by Distance")

# Show the plot
plt.grid(True)
plt.show()
