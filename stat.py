def stat( data ):
  totalsum = 0
  #Suma de los numeros
  for i in data:
    totalsum += i

  #Mean or Average
  N = len( data )
  mean = totalsum / N

  return totalsum, mean


data = [1, 5, 6, 3, 12, 3]
totalsum, mean = stat(data)

print( totalsum, mean )
  
