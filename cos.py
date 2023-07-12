import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
y = np.cos(x)
z = np.sin(x)

plt.plot(x,y, '--g', label="cos(x)")
plt.plot(x,z, label="sin(x)")
plt.title('Esto es un coseno y seno de x')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()
