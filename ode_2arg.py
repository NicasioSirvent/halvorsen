# dx/dt = ax + b
# a = -1/T; b = 1; T = 5; x0 = 1
# Probar con distintos a's y b's

#vamor a ver.. aproximacion "burda"
# dx/dt(1) ~~ 1 - 0.2 + 1 -> 1.8; inc:.8
# dx/dt(2) ~~  1.8 - 0.2*1.8 + 1 -> 2.8 - 0.36 -> 2.44 -> inc:.64
# dx/dt(3) ~~ 2.44 - 0.2*2.44 + 1 -> 3.44 - 0.49 -> 2.95 -> inc:.51
# -> la pendiente va bajando... al final ~ 0.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = 0
tstop = 25
increment = 1

x0 = 1
T = 5
a = -1/T
b = 1
t = np.arange( tstart, tstop+1, increment )

#funcion que retorna dx/dt
def mydiff(x, t, a, b):
    dxdt = a * x + b
    return dxdt

#solve ode
x = odeint( mydiff, x0, t, args=(a,b,) )
print(x)

a = -2/T
b = 1
y = odeint( mydiff, x0, t, args=(a,b,) )

a = -1/T
b = 0
z = odeint( mydiff, x0, t, args=(a,b,) )


plt.plot( t, x, label='a = -0.2; b = 1' )
plt.plot( t, y, label='a = -0.4; b = 1' )
plt.plot( t, z, label='a = -0.2; b = 0' )

plt.title('dx/dt = ax + b')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.legend()
plt.show()