import numpy as np
 
# using loadtxt()
distances = np.loadtxt("distances.csv", delimiter=',')
points = np.loadtxt("points.csv", delimiter=',')

print(distances,type(distances[0]))