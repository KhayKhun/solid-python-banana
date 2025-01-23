import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("values_for_bars.csv", delimiter=',')

count = {}

for d in data:
    if d in count:
        count[int(d)] += 1
    else:
        count[int(d)] = 1

numbers = count.keys()
frequencies = count.values()

fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(x=numbers, height=frequencies, width=0.8, edgecolor="black", linewidth=1)

ax.set_xlim(min(numbers) - 0.5, max(numbers) + 0.5)  # adjust spacing, cus 1 and 10 are showing only half
ax.set_ylim(0, max(frequencies) + 1)

ax.set_xlabel("Number")
ax.set_ylabel("Count")
ax.set_title("Bar Chart of Value Frequencies")

ax.grid(axis="y") # show gird only in y axis
plt.show()
