# dx/dt = -ax + bu
# u:señal de control; a, b: ctes
# Probar con distintos a's, b's y u's

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = 0
tstop = 25
increment = 1

a = 0.25
b = 2
u = 1
x0 = 1

t = np.arange( tstart, tstop+1, increment )

#funcion que retorna dx/dt
def mydiff(x, t, a, b, u):
    dxdt = -a * x + b * u
    return dxdt

#solve ode
x = odeint( mydiff, x0, t, args=(a,b,u,) )
print(x)

a = 0.5
b = 2
u = 1
y = odeint( mydiff, x0, t, args=(a,b,u,) )

a = 0.25
b = 2
u = 2
z = odeint( mydiff, x0, t, args=(a,b,u,) )


a = 0.25
b = 0.2
u = 1
v = odeint( mydiff, x0, t, args=(a,b,u,) )

plt.plot( t, x, label='a = .2; b = 2; u = 1' )
plt.plot( t, y, label='a = .5; b = 2; u = 1' )
plt.plot( t, z, label='a = .2; b = 2; u = 2' )
plt.plot( t, v, label='a = .2; b = .2; u = 1' )

plt.title('dx/dt = -ax + bu; u:control input')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.legend()
plt.show()