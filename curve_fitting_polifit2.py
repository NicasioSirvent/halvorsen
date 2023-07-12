#ahora con np polifit (antes era scypi's curve_fit)
# ejercicio fin capitulo
from matplotlib import pyplot as plt
import numpy as np


x = [10,20,30,40,50,60,70,80,90,100]
y = [23,45,60,82,111,140,167,198,200,220]



xstart = 0
xstop = 120
xstep = 10
xmodel = np.arange(xstart, xstop, xstep)

startorder = 1
endorder = 5

for modelorder in range(startorder, endorder, 1):
    p = np.polyfit(x, y, modelorder)  #np.polyfit para polyfitting
    print( p )
    ymodel = np.polyval(p, xmodel)  #np.polyval para los valores!
    plt.subplot(2,2,modelorder)
    plt.plot(x, y, 'or')
    plt.plot(xmodel, ymodel)
    plt.title('Fitting Orden ' + str(modelorder))

plt.legend()
plt.show()