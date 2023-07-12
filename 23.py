import math

def uno( x, y ):
  #z = 3x² + (x² + y²)^(1/2) + e^(ln(x))
  z = 3*math.pow(x,2) + math.pow( math.pow( x,2) \
        + math.pow(y,2), 1/2) + math.exp(math.log(x))
  return z
