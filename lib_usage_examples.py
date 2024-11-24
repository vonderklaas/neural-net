import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**2 - 4*x + 5

xs = np.arange(-5, 5, 0.25)
ys = f(xs)

# Create the plot
plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of f(x) = 3x^2 - 4x + 5")
plt.show()

# Derivative?
h = 0.01
x = 3.0
print(f(x + h) - f(x)) # 0.14029999999999632