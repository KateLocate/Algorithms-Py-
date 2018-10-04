# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

START = -1000
STOP = 1000

list_1 = [random.randint(START, STOP) for _ in range(10)]
print(list_1)

maximum = START

for i, item in enumerate(list_1):

    if item < 0:

        if maximum < item:
            maximum = item

print(f'Maксимальное отрицательное число: {maximum}.')