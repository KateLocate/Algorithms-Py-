# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
#  (оба являться минимальными), так и различаться.

import random

list_1 = [random.randint(0, 100) for _ in range(10)]
print(list_1)

# не смогла придумать решение за один цикл без метода сортировки :(

minimum_1 = 100
minimum_2 = 100

for i, item in enumerate(list_1):

    if item < minimum_1:
        minimum_1 = item

for i, item in enumerate(list_1):

    if minimum_1 < item < minimum_2:
        minimum_2 = item

print(f'Два наименьших числа списка: {minimum_1}, {minimum_2}')
