primo = list()
#primo solo tiene al 1 y a si mismo como divisor
#me salto al 1
for i in range(2,200):
  #print("i:", i)
  for k in range (2,i+1):
    #print("k:", k)
    #si no es divisor, sigo buscando un divisor
    if (i % k != 0):
      continue
    #si es divisor natural != a el mismo, lo descarto.
    elif (i % k == 0) and (i != k):
      break
    else:
      #si cumple (es divisor y no es el mismo.
      #print("append")
      primo.append(i)
      break
  
    


print(primo)
