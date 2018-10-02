# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(0, 100) for _ in range(4)] for _ in range(4)]
minimum_values = [0]*4

for line in matrix:

    for i, item in enumerate(line):

        print(f'{item:>4}', end='')

    print('')

n = 0

while n < 4:
    i = 0
    minimum = 100

    while i < 4:
        if matrix[i][n] < minimum:
            minimum = matrix[i][n]
            minimum_values[n] = matrix[i][n]
        i += 1

    n += 1

maximum = 0

print('Минимальные значения из каждого столбца:')

for i, item in enumerate(minimum_values):

    print(f'{item:>4}', end='')

    if item > maximum:
        maximum = item

print(f'\nМаксимальное среди минимальных значений: \n{maximum:>10}')
