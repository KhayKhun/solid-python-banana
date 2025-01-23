import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.sin(2*x)

x = np.linspace(-10, 10, 400)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, linestyle='dashed', label=r'$f(x) = x \cdot \sin(2x)$', color='red')  # \cdot -> . instead of *

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'$Graph \ of \ f(x) = x \cdot \sin(2x)$')

plt.grid(True)
plt.legend()
plt.show()
