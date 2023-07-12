N = 10

fib = [0, 1]

for i in range(N-2):
  fib_next = fib[i+1] + fib[i]
  fib.append(fib_next)

print(fib)
