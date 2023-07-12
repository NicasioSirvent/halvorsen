import math

def average( x, y ):
  return (x + y) / 2

def calAverage( x, y ): #Sin return
  print ( (x + y) / 2 )
  return

def d2r( g ):
  return g * math.pi/180

def r2d( r ):
  return r * 180 / math.pi

def fib ( n ):
  a, b = 0, 1
  while a < n :
    print(a, end=' ')
    a, b = b, a + b

def checkifprime( n ):
  #buscamos divisor desde 2 hasta él mismo. (range(5)-> 0-4....)
  for x in range( 2, n+1 ):
    if n%x != 0: #si no divisor natural, seguimos buscando.
      continue
    elif n%x == 0 and n != x: #encontramos divisor! -> False
      return False
    else:  #hemos llegado a el mismo sin encontrar divisor: True
      return True
