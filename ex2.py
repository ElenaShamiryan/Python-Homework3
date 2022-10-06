import random

n = int(input('Введите длину списка: '))
list = []


def first_list(list):
    for i in range(n):
        num = random.randint(-10, 10)
        list.append(num)
    print(f'Исходный  список: {list}')


def new_list(list, n):
    if n % 2 == 0:
        for i in range(n//2):
            mult = list[i] * list[n-1 - i]
            print(mult, end=' ')
    else:
        for i in range((n+1)//2):
            mult = list[i] * list[n-1 - i]
            print(mult, end=' ')


first_list(list)
new_list(list, n)
