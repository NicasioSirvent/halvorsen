# dx/dt = ax;
# a = -1/T ; (T->time constant = 5)
# solucion: x(t) = e^(at) * xo;
# (Xo, posicion inicial, = 1)
# solucion 0 <= t <= 25
#grid, title, labels,

import matplotlib.pyplot as plt
import numpy as np

a = - 1 / 5
xo = 1


t = np.arange( 0, 25, 0.1)
x = np.exp( t*a ) * xo

plt.plot( t, x, 'r', label='xx')
plt.title('Un Sistema Dinámico: dx/dt=ax')
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.legend()
plt.show()
