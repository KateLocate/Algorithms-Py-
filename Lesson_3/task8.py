# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
#  введенных элементов каждой строки и записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.

print('Заполним матрицу 4х4. Вводите элементы по одному.')

SIZE = 4

matrix = [[None for i in range(SIZE)] for _ in range(SIZE)]
i = 0

while i < SIZE:
    n = 0

    while n < SIZE:
        matrix[i][n] = int(input(f'Ряд {i+1}, ячейка {n+1}:'))
        n += 1

    i += 1


for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        sum_line += item

        print(f'{item:>3}', end='')

    print(f'  | {sum_line}')
