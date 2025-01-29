import random
import time
import numpy as np
import matplotlib.pyplot as plt

def generate_random_segments(num_segments, x_min=0, x_max=10, y_min=0, y_max=10, seed=42):
    random.seed(seed)
    segments = []
    for _ in range(num_segments):
        x1 = random.uniform(x_min - 5, x_max + 5)
        y1 = random.uniform(y_min - 5, y_max + 5)
        x2 = random.uniform(x_min - 5, x_max + 5)
        y2 = random.uniform(y_min - 5, y_max + 5)
        segments.append([x1, y1, x2, y2])
    return segments

def filter_segments_python(segments, x_min=0, x_max=10, y_min=0, y_max=10):

    filtered = []
    for seg in segments:
        x1, y1, x2, y2 = seg
        if (x_min <= x1 <= x_max and
            x_min <= x2 <= x_max and
            y_min <= y1 <= y_max and
            y_min <= y2 <= y_max):
            filtered.append(seg)
    return filtered

def measure_time_python(segments, x_min=0, x_max=10, y_min=0, y_max=10):

    t0 = time.time()
    filtered = filter_segments_python(segments, x_min, x_max, y_min, y_max)
    t1 = time.time()
    return filtered, (t1 - t0)

def filter_segments_numpy(segments_array, x_min=0, x_max=10, y_min=0, y_max=10):
    valid_x1 = (segments_array[:, 0] >= x_min) & (segments_array[:, 0] <= x_max)
    valid_y1 = (segments_array[:, 1] >= y_min) & (segments_array[:, 1] <= y_max)
    valid_x2 = (segments_array[:, 2] >= x_min) & (segments_array[:, 2] <= x_max)
    valid_y2 = (segments_array[:, 3] >= y_min) & (segments_array[:, 3] <= y_max)
    mask = valid_x1 & valid_y1 & valid_x2 & valid_y2
    return segments_array[mask]

def measure_time_numpy(segments_array, x_min=0, x_max=10, y_min=0, y_max=10):
    t0 = time.time()
    filtered_array = filter_segments_numpy(segments_array, x_min, x_max, y_min, y_max)
    t1 = time.time()
    return filtered_array, (t1 - t0)

def main():
    num_segments = 100000
    segments = generate_random_segments(num_segments)

    x_min, x_max, y_min, y_max = 0, 10, 0, 10

    # plain python
    filtered_py, time_py = measure_time_python(segments, x_min, x_max, y_min, y_max)

    # numpy
    segments_np = np.array(segments)
    filtered_np, time_np = measure_time_numpy(segments_np, x_min, x_max, y_min, y_max)

    print(f"Python: {len(filtered_py)} remain, time: {time_py}")
    print(f"NumPy: {len(filtered_np)} remain, time: {time_np}")

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # all lines (left)
    axes[0].set_title("All Lines")
    for seg in segments:
        x1, y1, x2, y2 = seg
        axes[0].plot([x1, x2], [y1, y2])
    axes[0].set_xlim(x_min - 5, x_max + 5)
    axes[0].set_ylim(y_min - 5, y_max + 5)

    # filtered lines (right)
    axes[1].set_title("Filtered Lines")
    for seg in filtered_py:
        x1, y1, x2, y2 = seg
        axes[1].plot([x1, x2], [y1, y2])
    axes[1].set_xlim(x_min - 1, x_max + 1)
    axes[1].set_ylim(y_min - 1, y_max + 1)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()