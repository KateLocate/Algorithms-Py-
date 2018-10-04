# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

START = 0
STOP = 1000000

list_1 = [random.randint(START, STOP) for _ in range(10)]
print(list_1)

minimum = STOP
maximum = START

for i, item in enumerate(list_1):

    if item >= maximum:
        maximum = item
        a = i

    if item <= minimum:
        minimum = item
        b = i

list_1[a], list_1[b] = minimum, maximum
print(list_1)