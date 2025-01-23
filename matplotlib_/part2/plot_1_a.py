import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * y

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y) # create 2D grid

print(X, Y)
Z = f(X, Y)

# Create a 3D surface plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(X, Y, Z, cmap='cool', edgecolor='none')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z = f(x, y)")
ax.set_title("3D Surface Plot of f(x, y) = x * y")

plt.show()
