# Fuerza F hacia abajo, sobre masa colgando de muelle(k) y amortiguada en fluido(c)
# d2x/dt2 = F(t) - c*dx/dt - k*x
# cambio de variables: x1 = x; x2 = dx/dt
#  dx1/dt = x2
#  dx2/dt = F(t) - c*x2 - k*x1
# Probar con distintos F's, c's y k's

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = 0
tstop = 10
increment = 0.1

F = 1
c = 1
k = 1
x_init = [0, 0]

t = np.arange( tstart, tstop+1, increment )

#funcion que retorna dx/dt
def mydiff(x, t, F, c, k):
    dx1dt = x[1]
    dx2dt = F - c*x[1] - k*x[0]
    dxdt = [dx1dt, dx2dt]
    return dxdt

#solve ode
x = odeint( mydiff, x_init, t, args=(F,c,k,) )
print(x)

x1 = x[:,0]

F = 2
c = 1
k = 1
y = odeint( mydiff, x_init, t, args=(F,c,k,) )
y1 = y[:,0]

F = 1
c = 1
k = 3
z = odeint( mydiff, x_init, t, args=(F,c,k,) )
z1 = z[:,0]

F = 1
c = 2
k = 1
v = odeint( mydiff, x_init, t, args=(F,c,k,) )
v1 = v[:,0]
plt.plot( t, x1, label='F=1; c=1; k=1' )
plt.plot( t, y1, label='F=2; c=1; k 1' )
plt.plot( t, z1, label='F=1; c=1; k=3' )
plt.plot( t, v1, label='F=1; c=2; k=1' )

plt.title('d2x/dt2 = F(t) - c*dx/dt - kx')
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.legend()
plt.show()