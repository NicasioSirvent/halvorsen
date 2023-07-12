#uso de scypi.trapz para calcular integral
from scipy import integrate
import numpy as np

a = -1
b = 1
N = 100  # al cambiar 10 por 100 se aproxima mucho mas.
dx = (b - a)/N

x = np.linspace(a, b, N + 1)
#x = np.arange(a, b+dx, dx) # tambien usable .. 
#y = x**2
#y = x**3 + 2*x**2 - x + 3
y = np.sin(x)

I = integrate.trapz(y, x, dx)
print(I)
