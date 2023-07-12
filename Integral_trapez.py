#uso de regla trapezoidal (cuadrado + triangulo) para encontrar integral
# cada trozo: y0Ax + 1/2 (y1-y0)Ax -> (y0 + y1)Ax/2
#  todo: Ax/2 * sumat(1..N) (f(x)i + f(x)i+1)

import numpy as np

a = 0
b = 1
N = 10

# el N+1 es para que de 0 0.1 0.2 .... 1 (11 valores), si N: 0 1.1 2.2 3.3 ... 10 (10 valores)
x = np.linspace(a, b, N+1)
#print(x)
y = x**2
#print(y)

#np.sum ira sumando y_right[i] + y_left[i]...
y_right = y[1:] 
#print(y_right)
y_left = y[:-1]
#print(y_left)

dx = (b - a)/N
A = (dx/2) * np.sum(y_left + y_right)
#print(A)

