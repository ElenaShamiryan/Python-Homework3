import random


n = int(input('Введите длину списка: '))
list = []


def first_list(list):
    for i in range(n):
        num = round(random.random()*10, 2)
        list.append(num)
    print(f'Исходный  список: {list}')


def second_list(list):  
    sec_list = []
    for i in range(n):
        result = round((list[i] % 1), 2)
        sec_list.append(result)
    return sec_list


first_list(list)
mult_list = second_list(list)
print(f'Дробный   список: {mult_list}')


max = mult_list[0]
min = mult_list[0]

for i in range(n):
    if mult_list[i] > max:
        max = mult_list[i]
    elif mult_list[i] < min:
        min = mult_list[i]

dif = round(max - min, 2)
print(f'Разница между наибольшей и наименьшей дробной частью равна {dif}')
