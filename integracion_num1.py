#de ejercicio pag 201
#usando integrate.quad

from scipy import integrate
import numpy as np

def y(x):
    return x**3 + 2*x**2 - x + 3
#    return np.sin(x)
a = -1
b = 1

Y = integrate.quad(y, a, b)
print(Y)