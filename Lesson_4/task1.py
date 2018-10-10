# Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания первых
#  трех уроков.

# 3.9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
import cProfile


def max_in_min(size):

    START = 0
    STOP = 100

    minimum = STOP
    maximum = START

    matrix = [[random.randint(START, STOP) for _ in range(size)] for _ in range(size)]
    minimum_values = [0]*size

    for j in range(size):

        for i in range(size):
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]
                minimum_values[j] = matrix[i][j]

    for i, item in enumerate(minimum_values):

        if item > maximum:
            maximum = item

# Данные по скорости работы max_in_min:

# 5000 loops, best of 5: 71.8 usec per loop - 5
# 50 loops, best of 5: 5.59 msec per loop - 50
# 1 loop, best of 5: 583 msec per loop - 500

# Скорость выполнения алгоритма падает не линейно: увеличение размера матрицы на один элемент
# дает прирост в длительности выполнения в 10 раз.
# Сложность алгоритма линейная: t = 10n?


def max_from_min(size):

    START = 0
    STOP = 100

    minimum = STOP

    matrix = [[random.randint(START, STOP) for _ in range(size)] for _ in range(size)]
    minimum_values = [0]*size

    for j in range(size):

        for i in range(size):
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]
                minimum_values[j] = matrix[i][j]

    maximum = max(minimum_values)

# Данные по скорости работы max_from_min:

# 5000 loops, best of 5: 66.5 usec per loop - 5
# 50 loops, best of 5: 5.48 msec per loop - 50
# 1 loop, best of 5: 558 msec per loop - 500

# Скорость выполнения алгоритма практически не изменяется по сравнению с предыдущим вариантом функции. Замена цикла
#  с условием на встроенную функцию max не влияет на скорость.
# Сложность алгоритма линейная: t = 10n?


def max_by_sort(size):

    base = [[random.randint(0, 100) for _ in range(size)] for _ in range(size)]

    matrix = [[None for _ in range(size)] for _ in range(size)]

    for i in range(size):

        for j, item in enumerate(matrix[i]):
            matrix[i][j] = base[j][i]

    maximum = float('-inf')

    for j in range(size):

        matrix[j].sort()

        if matrix[j][0] > maximum:
            maximum = matrix[j][0]

# Данные по скорости работы max_by_sort:

# 5000 loops, best of 5: 68.5 usec per loop - 5
# 50 loops, best of 5: 5.59 msec per loop - 50
# 1 loop, best of 5: 580 msec per loop - 500

# Скорость выполнения алгоритма практически не изменяется по сравнению с предыдущими вариантами функции. Метод .sort()
#  не ускорил и не замедлил выполнение.
# Сложность алгоритма линейная: t = 10n?


# Оценка количества вызовов самой функции через cProfile тут не пригодилась, в каждом из случаев она вызывается лишь
#  однажды.
# Интересно было наблюдать за тем, как возрастало количество вызовов функций для генерации случайных чисел, например:

# cProfile.run('max_by_sort(1000)')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)

#         1    0.011    0.011    3.370    3.370 <string>:1(<module>)
#   1000000    1.015    0.000    2.114    0.000 random.py:174(randrange)
#   1000000    0.431    0.000    2.545    0.000 random.py:218(randint)
#   1000000    0.772    0.000    1.098    0.000 random.py:224(_randbelow)
#         1    0.219    0.219    3.360    3.360 task1.py:74(max_by_sort)
#         1    0.003    0.003    2.941    2.941 task1.py:76(<listcomp>)
#         1    0.001    0.001    0.070    0.070 task1.py:78(<listcomp>)
#         1    0.000    0.000    3.371    3.371 {built-in method builtins.exec}
#   1000000    0.091    0.000    0.091    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1267692    0.236    0.000    0.236    0.000 {method 'getrandbits' of '_random.Random' objects}
#      1000    0.131    0.000    0.131    0.000 {method 'sort' of 'list' objects}

# То есть время выполнения функции во всех случаях возрастает в основном из-за генератора списка
#  на основе модуля random?


# Похоже, улучшить код могу только визуально... Количество циклов не меняется)) Хотя если Вы говорили, что для матриц
#  их количество сложно сократить, то может еще ничего)
