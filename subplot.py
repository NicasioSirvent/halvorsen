import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x,y,'g')
plt.title('Sin')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()

plt.subplot(2,1,2)
plt.plot(x,z,'r')
plt.title('Cos')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid()
plt.show()
