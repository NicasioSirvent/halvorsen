#ejercicio pag 203
#encontrar trabajo pv al expandirse un embolo...
#suponer gas ideal.
# w = integral(vf-vi) PdV

from scipy import integrate

v1 = 3 #m3
v2 = 5 #m3



# P = nRT/V
def f(x):
    return 8.31 * 300 / x

Y = integrate.quad(f, v1, v2)
print(Y) # -> 1273

# comprobacion: proceso expansion isotermico: PV = cte
# W(1->2) = nRT ln(V2/V2) = 1273 (calculadora) -> perfecto!

