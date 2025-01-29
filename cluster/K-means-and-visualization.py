import random
import time
import matplotlib.pyplot as plt

def generate_data(centroids, points_per_centroid=300):

    all_points = []
    for (cx, cy) in centroids:
        for _ in range(points_per_centroid):
            x = random.gauss(cx, 1.0)
            y = random.gauss(cy, 1.0)
            all_points.append((x, y))
    return all_points

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def initialize_centroids(points, k):
    random_centroids = random.sample(points, k)
    return [(c[0], c[1]) for c in random_centroids]

def assign_clusters(points, centroids):
    labels = []
    for p in points:
        min_dist = float('inf')
        cluster_index = -1
        for i, c in enumerate(centroids):
            dist = distance(p, c)
            if dist < min_dist:
                min_dist = dist
                cluster_index = i
        labels.append(cluster_index)
    return labels

def recompute_centroids(points, labels, k):
    sums_x = [0.0] * k
    sums_y = [0.0] * k
    counts = [0] * k
    
    # Accumulate sums
    for (p, lbl) in zip(points, labels):
        sums_x[lbl] += p[0]
        sums_y[lbl] += p[1]
        counts[lbl] += 1

    # calculate new centroids
    new_centroids = []
    for i in range(k):
        new_centroids.append((sums_x[i] / counts[i], sums_y[i] / counts[i]))
            
    return new_centroids

def kmeans_plain_python(points, k, max_iter=500):
    centroids = initialize_centroids(points, k)
    for _ in range(max_iter):
        labels = assign_clusters(points, centroids)
        new_centroids = recompute_centroids(points, labels, k)
        centroids = new_centroids
    
    return centroids, labels

# K-means with NumPy
import numpy as np

def kmeans_numpy(points, k, max_iter=500):

    arr = np.array(points)    
    random_indices = np.random.choice(len(points), k, replace=False)
    centroids = arr[random_indices, :]
    
    for _ in range(max_iter):
        diff = arr[:, np.newaxis, :] - centroids[np.newaxis, :, :]
        dist_sq = np.sum(diff**2, axis=2) 
        labels = np.argmin(dist_sq, axis=1)
        
        new_centroids = []
        for i in range(k):
            cluster_points = arr[labels == i]
            if len(cluster_points) == 0:
                new_centroids.append([random.random()*10, random.random()*10])
            else:
                new_centroids.append(cluster_points.mean(axis=0))
                
        centroids = np.array(new_centroids)
    
    return centroids, labels


def main():
    true_centroids = [(3, 3), (7, 7), (2, 8)]
    k = 3
    points_per_centroid = 300

    points = generate_data(true_centroids, points_per_centroid)
    
    plt.figure(figsize=(6, 6))
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    plt.scatter(xs, ys, s=10, alpha=0.5)
    cx = [c[0] for c in true_centroids]
    cy = [c[1] for c in true_centroids]
    plt.scatter(cx, cy, c="red", marker="x", s=100, label="Original Centroids")
    plt.title("Initial data + 'True' centroids (before k-means)")
    plt.legend()
    plt.savefig("Image 1.png")
    plt.close()
    
    # K-means with plain Python
    start_time = time.time()
    final_centroids_py, labels_py = kmeans_plain_python(points, k, max_iter=500)
    end_time = time.time()
    py_time = end_time - start_time
    print(f"Plain Python {py_time:.4f} seconds.")
    
    colors = ["blue", "green", "orange", "purple", "gray", "cyan"]
    
    plt.figure(figsize=(6,6))
    for cluster_id in range(k):
        cluster_points = [p for (p, lbl) in zip(points, labels_py) if lbl == cluster_id]
        xs = [cp[0] for cp in cluster_points]
        ys = [cp[1] for cp in cluster_points]
        plt.scatter(xs, ys, s=10, alpha=0.5, c=colors[cluster_id % len(colors)], label=f"Cluster {cluster_id}")
    
    cx = [c[0] for c in final_centroids_py]
    cy = [c[1] for c in final_centroids_py]
    plt.scatter(cx, cy, c="red", marker="x", s=200, label="K-means Centroids")
    
    plt.title("K-means Result (Plain Python)")
    plt.legend()
    plt.savefig("Image 2.png")
    plt.close()
    
    # K-means with numpy
    start_time = time.time()
    final_centroids_np, labels_np = kmeans_numpy(points, k, max_iter=500)
    end_time = time.time()
    np_time = end_time - start_time
    print(f"Numpy {np_time:.4f} seconds.")
    
    plt.figure(figsize=(6,6))
    arr = np.array(points)
    for cluster_id in range(k):
        cluster_points = arr[labels_np == cluster_id]
        plt.scatter(cluster_points[:,0], cluster_points[:,1],
                    s=10, alpha=0.5,
                    c=colors[cluster_id % len(colors)], label=f"Cluster {cluster_id}")
    
    plt.scatter(final_centroids_np[:,0], final_centroids_np[:,1],
                c="red", marker="x", s=200, label="K-means Centroids (NP)")
    plt.title("K-means Result (NumPy)")
    plt.legend()
    plt.savefig("kmeans_result_np.png")
    plt.close()
    
if __name__ == "__main__":
    main()