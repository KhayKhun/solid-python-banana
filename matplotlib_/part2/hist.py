import numpy as np
import matplotlib.pyplot as plt

values = np.loadtxt("values_for_hist.csv", delimiter=',')

plt.figure(figsize=(8, 6))
plt.hist(values, bins=10, color='blue', edgecolor='black', alpha=0.7)  # group the range into 10 bins

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Given Values")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()