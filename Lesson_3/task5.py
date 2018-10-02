# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

list_1 = [random.randint(-1000, 1000) for _ in range(10)]
print(list_1)

maximum = -1000

for i, item in enumerate(list_1):

    if item < 0:

        if maximum < item:
            maximum = item

print(f'Maксимальное отрицательное число: {maximum}.')