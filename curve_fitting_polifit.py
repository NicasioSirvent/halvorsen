#ahora con np polifit (antes era scypi's curve_fit)
from matplotlib import pyplot as plt
import numpy as np


x = [0,1,2,3,4,5]
y = [15,10,9,6,2,0]
plt.plot(x, y, 'or')


xstart = -1
xstop = 6
xstep = 0.1
xmodel = np.arange(xstart, xstop, xstep)

startorder = 1
endorder = 5

for modelorder in range(startorder, endorder, 1):
    p = np.polyfit(x, y, modelorder)  #np.polyfit para polyfitting
    print( p )
    ymodel = np.polyval(p, xmodel)  #np.polyval para los valores!
    plt.plot(xmodel, ymodel, label='orden:'+str(modelorder))

plt.legend()
plt.show()