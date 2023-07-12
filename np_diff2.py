#ejercicio: pag 191
#encontrar derivada numericamente.
# y = x^3 + 2x^2 - x + 3
# y = sin(x)
# y = x^5 - 1

#varias aproximaciones... 10 puntos y 100 puntos.
#np.diff devuelve array-1, y plot pide que x sea = size que y, asi que arreglar...

from matplotlib import pyplot as plt
import numpy as np

xstart = -5
xstop = 5.1
increment = 0.1

x = np.arange( xstart, xstop, increment )
#y = x**3 + 2*(x**2) - x + 3
#y = np.sin(x)
y = x**5 - 1

#dydx_exact = 3*(x**2) + 4*x - 1
#dydx_exact = np.cos(x)
dydx_exact = 5 * x**4

plt.plot(x, dydx_exact, 'r', label='derivada exacta')

dydx_num = np.diff(y) / np.diff(x)
#print(len(dydx_num))
xstart = -5
xstop = 5
increment = 0.1 # jugar con distintos incrementos para ver como se aproxima...
x = np.arange(xstart, xstop, increment)
#print(len(x))

plt.plot(x, dydx_num, label='derivada numerica')
plt.legend()
plt.show()
