# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

list_1 = [random.randint(0, 100) for _ in range(10)]
print(list_1)

maximum = 0
minimum = 100

for i, item in enumerate(list_1):

    if item > maximum:
        maximum = item
        a = i

    if minimum > item:
        minimum = item
        b = i

if a < b:
    index = a + 1
    summa = 0

    while b > index:
        summa += list_1[index]
        index += 1

else:
    index = b + 1
    summa = 0

    while a > index:
        summa += list_1[index]
        index += 1

print(f'Минимальное значение из списка: {minimum}, позиция - {b}, \nмаксимальное: {maximum}, позиция - {a}')
print(f'Сумма всех значений между максимальным и минимальным равна {summa}')