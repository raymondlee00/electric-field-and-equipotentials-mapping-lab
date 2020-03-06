import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

x = np.linspace(0, 5, 50) 
y = np.linspace(0, 5, 40)

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

X, Y = np.meshgrid(x, y, indexing="ij")
Z = f(X, Y)

pprint("Z type: {}".format(type(Z)))

plt.contour(X, Y, Z, colors="black")

plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("learning matplotlib and numpy")
plt.legend(['Sine', 'Cosine'])
plt.show()


X_1, Y_1 = np.meshgrid(x, y, indexing="xy")
pprint("X_1: {}".format(X_1))
pprint("Y_1: {}".format(Y_1))

X_2, Y_2 = np.meshgrid(x, y, indexing="ij")
pprint("X_2: {}".format(X_2))
pprint("Y_2: {}".format(Y_2))
pprint("Z: {}".format(Z))