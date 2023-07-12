primo = list()
#primo solo tiene al 1 y a si mismo como divisor
#me salto al 1
for i in range(2,200):
  for k in range (2,i+1):
    if (i % k == 0):  #Si hay divisor
      if (i != k):  # y no el mismo, no es primo. Pasar a siguiente...
        break
      else:  # Si él mismo... al sac.
        primo.append(i)
        break    
print(primo)
