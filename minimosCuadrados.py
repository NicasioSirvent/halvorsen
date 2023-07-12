#minimos cuadrados... Y = Phi * Theta; Y conocido, Phi matriz regresion, Theta matriz a encontrar
#encontrar Phi / minimo ...
#  Theta(ls) = (Phi^t*Phi)^-1*Phi^t*Y
#  Aqui: y(1) = 0.8 ; y(2) = 3.0; y(3) = 4;
#  [0.8]   [1 1]   [a]
#  [3]   = [2 1] * [b]
#  [4]     [3 1]

import numpy as np
#varias manera de hacer... operaciones con matrices o metodos directos...
#pruebo
#puta coma... media hora perdida...

Phi = np.array([ [1, 1],
                 [2, 1],
                 [3, 1] ], dtype='float64' )

Y = np.array([[0.8],[3.0],[4.0]])

Theta = np.array([ [0], [0] ])
Theta = np.linalg.lstsq( Phi, Y, rcond=None )[0]
print(Theta)
