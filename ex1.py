import random

n = int(input('Введите длину списка: '))
list = []


def first_list(list):
    for i in range(n):
        num = random.randint(-10, 10)
        list.append(num)
    print(f'Исходный  список: {list}')


def sum_of_elements(list, n):
    sum = 0
    for i in range(1, n, 2):
        sum = sum + list[i]
    return sum


first_list(list)
odd_num = sum_of_elements(list, n)
print(f'Сумма чисел на нечетных позициях равна {odd_num}')
