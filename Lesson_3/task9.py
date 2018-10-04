# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

START = 0
STOP = 100
SIZE = 4

matrix = [[random.randint(START, STOP) for _ in range(SIZE)] for _ in range(SIZE)]
minimum_values = [0]*SIZE

for line in matrix:

    for i, item in enumerate(line):

        print(f'{item:>4}', end='')

    print('')

n = 0

while n < SIZE:
    i = 0
    minimum = STOP

    while i < SIZE:
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
