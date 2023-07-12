import math

def uno( x, y ):
  #z = 3x² + (x² + y²)^(1/2) + e^(ln(x))
  z = 3*math.pow(x,2) + math.pow( math.pow( x,2) \
        + math.pow(y,2), 1/2) + math.exp(math.log(x))
  return z

def dos( x ):
  a=1
  b=3
  c=5
  num = math.log(a*math.pow(x, 2) + b*x + c) - math.sin(a*math.pow(x,2) + b*x + c)
  den = 4*math.pi*pow(x,2) + math.cos(x - 2)*(a*pow(x,2) + b*x + c)
  return num/den

def pitagoras( a, b ):
  return math.pow(math.pow(a,2) + math.pow(b,2), 1/2)

def sol():
  # el sol radia 385*10^24 J/s
  #a) cuanta masa pierde por dia? (e = mc^2)
  # Julios al dia?
  jd = 385*math.pow(10,24)*60*60*24
  #a masa..
  md = jd / ( 9*pow(10,16) )
  print("El sol pierde", md, " kg al dia" )
  #b) cuantos años durara? (m= 2*10^30kg)
  #kg al año?
  ad = 2*math.pow(10,30) / ( md * 365 )
  print("El sol durara", ad, "años")
  
