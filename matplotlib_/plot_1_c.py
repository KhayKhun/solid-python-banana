import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.arctan(x)

x = np.linspace(-10, 10, 400)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, linestyle="dotted", label=r'$f(x) = \arctan x$', color='orange', )  # \cdot -> . instead of *

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'$Graph \ of \ f(x) = \arctan x$')

plt.grid(True)
plt.legend() # add some extra legend ui 
plt.show()
