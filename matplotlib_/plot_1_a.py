import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-10, 10, 400)
y = f(x) # ndarray

plt.figure(figsize=(8, 6))  # 8 inches, 6 inches
plt.plot(x, y, label=r'$f(x) = x^2$', color='blue')  # Plot with label, LATEX formating, use '$$' to make x^2 look beautiful

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of $f(x) = x^2$')

plt.grid(True)
plt.legend()

plt.show()
