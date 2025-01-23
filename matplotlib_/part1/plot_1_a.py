import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-10, 10, 20)
y = f(x) # ndarray data type

plt.figure(figsize=(8, 6))  # 8 inches, 6 inches
plt.plot(x, y, label=r'$f(x) = x^2$', color='green', marker="1", markerfacecolor="black", markeredgecolor="black")  # Plot with label, LATEX formating, use '$$' to make x^2 look beautiful

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of $f(x) = x^2$')

plt.grid(True)
plt.legend()
plt.show()