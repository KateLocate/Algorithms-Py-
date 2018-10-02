# 4. Определить, какое число в массиве встречается чаще всего.

import random

list_1 = [random.randint(0, 10) for _ in range(7)]
print(list_1)

value = 0
counter = 0
basis = list_1[0]


for i, item in enumerate(list_1):
    current_counter = 0

    for j, item_1 in enumerate(list_1):

        if item_1 == basis:
            current_counter += 1

        if counter <= current_counter:
            counter = current_counter
            value = basis

    basis = item

print(f'Чаще всего встречается число {value} - {counter} раз.')
