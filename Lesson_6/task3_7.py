# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
#  (оба являться минимальными), так и различаться.

import random
import task6_1 as t

START = 0
STOP = 100

lst = [random.randint(START, STOP) for _ in range(10)]
print(lst)

minimum_1 = STOP
minimum_2 = STOP

for i, item in enumerate(lst):

    if item < minimum_1:
        minimum_1 = item

for i, item in enumerate(lst):

    if minimum_1 < item < minimum_2:
        minimum_2 = item

print(f'Два наименьших числа списка: {minimum_1}, {minimum_2}')

t.show_total_size(START, STOP, lst, minimum_1, minimum_2)

# Размер всех объектов: 300-296
# В этой программе генерируется всегда одно и то же количество элементов, занимающих одинаковое количество памяти(за
#  исключением нуля).