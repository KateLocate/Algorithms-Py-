# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
#  Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
#  медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
#  который не рассматривался на уроках.

import random

M = 5
lst = [i for i in range(20)]
sample = random.choices(lst, k=2*M + 1)
print(sample)

mediana = 0
counter = True

for i, item in enumerate(sample):
    less = 0
    more = 0

    for j, item_j in enumerate(sample):

        if i != j:

            if item_j > item:
                more += 1

            elif item_j < item:
                less += 1

            else:
                if counter:
                    less += 1
                else:
                    more += 1
                counter = not counter

    if less == more:
        mediana = sample[i]
        break

print(mediana)
# print(sorted(sample))