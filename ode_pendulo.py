# Pendulo.
#  cambio de variables: x1 = x; x2 = dx/dt
# x = distancia desde centro (vertical), x1 = vel, x2 = accel. 
#  dx1/dt = x2
#  dx2/dt = - g * r / x1  - b * x2 / ( m * r**2 )
# (m)asa, r->longitud brazo, g->gravedad, b


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = 0
tstop = 1
increment = 0.1

m = 8
r = 5
b = 10
g = 1
x_init = [-0.5, 0] #x1->x, x2->dx/dt

t = np.arange( tstart, tstop+1, increment )

#funcion que retorna dx/dt
def mydiff(x, t, m, r, b):
    dx1dt = x[1]
    dx2dt = (- g * r / x[0] )  - ( (b * x[1] ) / ( m * (r**2) ) )
    dxdt = [dx1dt, dx2dt]
    return dxdt

#solve ode
x = odeint( mydiff, x_init, t, args=(m,r,b,) )
print(x)

x1 = x[:,0]

m = 2
r = 1
b = 0.1
#y = odeint( mydiff, x_init, t, args=(m,r,b,) )
#y1 = y[:,0]

m = 1
r = 2
b = 0.1
#z = odeint( mydiff, x_init, t, args=(m,r,b,) )
#z1 = z[:,0]

m = 1
r = 1
b = 0.3
#v = odeint( mydiff, x_init, t, args=(m,r,b,) )
#v1 = v[:,0]

plt.plot(t, x1)
#plt.plot( t, x1, label='8kg; 5m; roz=10' )
#plt.plot( t, y1, label='2kg; 1m; roz=.1' )
#plt.plot( t, z1, label='1kg; 2m; roz=.1' )
#plt.plot( t, v1, label='1kg; 1m; roz=.3' )

plt.title('d2x/dt2 = - g*r/x - b*(dx/dt) / ( m * r**2 )')
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.legend()
plt.show()