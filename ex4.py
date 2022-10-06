n = int(input('Введите число: '))

bin_num = ''
while n > 0:
    bin_num = str(n % 2) + bin_num
    n = n//2
print(bin_num)
