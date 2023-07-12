#ahora con np polifit (antes era scypi's curve_fit)
# ejercicio fin capitulo
from matplotlib import pyplot as plt
import numpy as np


x = [0, 1.7, 1.95, 2.60, 2.92, 4.04, 5.24]
y = [0, 2.6, 3.6, 4.03, 6.45, 11.22, 30.61]
plt.plot(x, y, 'or')



xstart = -1
xstop = 6
xstep = 0.1
xmodel = np.arange(xstart, xstop, xstep)

startorder = 1
endorder = 4

for modelorder in range(startorder, endorder, 1):
    p = np.polyfit(x, y, modelorder)  #np.polyfit para polyfitting
    ymodel = np.polyval(p, xmodel)  #np.polyval para los valores!
    plt.plot(xmodel, ymodel, label='orden:'+str(modelorder))

plt.legend()
plt.xlabel('Height(ft)')
plt.ylabel('Flow(ft³/s)')
plt.show()