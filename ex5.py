n = int(input('Введите число: '))
fib = [0, 1]

for i in range(n-1):
    fib.append(fib[-2] - fib[-1])

fib.reverse()

for k in range(n):
    fib.append(fib[-1]+fib[-2])

print(fib)
