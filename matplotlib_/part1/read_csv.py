import numpy as np
import matplotlib.pyplot as plt

distances = np.loadtxt("distances.csv", delimiter=',')
points = np.loadtxt("points.csv", delimiter=',')

# print(len(distances), distances) # 1D ndarray
# print(len(points), points) # 2D ndarray [x,y]

plt.figure(figsize=(8, 6)) # color in range -> c = distances
sc = plt.scatter(x=points[:, 0], y=points[:, 1], c=distances, cmap="cool")

plt.colorbar(sc, label="Distance Value")

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Points and Distances")

plt.grid(True)
plt.show()