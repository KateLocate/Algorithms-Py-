# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
#  15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля), т.к. именно в
#  этих позициях первого массива стоят четные числа.

import random
import task6_1 as t


list_1 = [random.randint(0, 1000000) for _ in range(10)]
print(list_1)
list_2 = []

for i, item in enumerate(list_1):

    if item % 2 == 0:
        list_2.append(i)

print('Индексы четных значений: ', list_2)

t.show_total_size(list_1, list_2)

# Размер всех объектов: 320, 288

# Очевидно, результат здесь зависит только от поведения модуля random, который может сгенерировать различное количество
# чётных значений(мне попалось 4 и 5). В него суммируются числа из списка исходных значений и списка индексов отобранных
# чётных чисел.
# Величина чисел исходного списка не влияет на занимаемый объем памяти (если число не равно нулю :) ), все они одного
# типа.
