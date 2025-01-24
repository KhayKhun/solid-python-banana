import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt("points.csv", delimiter=",")

x_min, x_max = points[:, 0].min(), points[:, 0].max()
y_min, y_max = points[:, 1].min(), points[:, 1].max()

# print(f"X bounds: ({x_min}, {x_max})") # X bounds: (-4.274337434585884, 6.516159455524173)
# print(f"Y bounds: ({y_min}, {y_max})") # Y bounds: (-4.381152698841351, 6.473180083946536)

def assign_clusters(points, centroids): # points + centroids = clusters
    # len(labels) = len(points)
    # labels[i] = points[i]'s cluster
    labels = []
    for p in points:
        distances = [np.abs(p[0] - c[0]) + np.abs(p[1] - c[1]) for c in centroids] # each index is each centroid
        # len(distances) = k
        labels.append(np.argmin(distances)) # np.argmin -> index of minimum distance

        # i.e. distances = [3, 4, 7, 8, 1, 0.2]
        # np.argmin(distances) -> 5, 5 is index of 0.2
    
    return np.array(labels)

def update_centroids(points, labels, k): # points -> (N, 2) # labels -> (N, ) shape
    centroids = []
    for i in range(k):
        cluster_points = points[labels == i] # all points in a cluster i
        """i.e
           points = np.array([
                [1, 2],  # Cluster 0
                [3, 4],  # Cluster 1
                [5, 6],  # Cluster 1
                [7, 8],  # Cluster 2
                [9, 10], # Cluster 0
                [11, 12] # Cluster 2
            ])
            labels = np.array([0, 1, 1, 2, 0, 2])

            cluster_points = points[labels == i]

            print(cluster_points)
            # Output:
            # [[3 4]
            #  [5 6]]  <- These are the points in Cluster 1
        """
        if len(cluster_points) > 0:
            centroids.append(cluster_points.mean(axis=0))
        else:
            centroids.append(points[i])  # Keep previous centroid if no points assigned
    return np.array(centroids)

def kmeans(points, k, gs):
    np.random.seed(gs)
    indices = np.random.choice(points.shape[0], k, replace=False) # points.shape[0] = num of rows, replace=False -> No duplicate
    centroids = points[indices] # 1. initialize first k centroids
    repeated = 0
    for _ in range(10): # repeat max 10 times
        repeated += 1
        labels = assign_clusters(points, centroids) # 2. assign clister
        # labels[i] = points[i]'s cluster

        new_centroids = update_centroids(points, labels, k) # move centroids
        if np.allclose(new_centroids, centroids): # don't move much? we good
            break
        centroids = new_centroids # else, continue
    
    print(f"Repeated {repeated} times.")
    
    return labels, centroids

K = 6 # clusters -> 0 to k -1
GUESSING_SEED = 42  # guessing seed
labels, centroids = kmeans(points, K, GUESSING_SEED)

plt.figure(figsize=(8, 6))

for i in range(K):
    cluster_points = points[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], s=30, label=f"Cluster {i + 1}")

plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c="black", marker="x", linewidths=3, label="Centroids")

plt.xlim(x_min - 1, x_max + 1)
plt.ylim(y_min - 1, y_max + 1)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple K-Means Simulation")
plt.legend()
plt.grid(True)

plt.show()
