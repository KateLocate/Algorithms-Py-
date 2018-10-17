# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
#  промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random


def bubble_sort(array):
    arr = array[:]
    n = 1

    while n < len(arr):

        for i in range(len(arr) - n):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        n += 1

        print(arr)

    print(arr)
    return arr


def bubble_sort_modified(array):
    arr = array[:]
    n = 1

    while n < len(arr):
        j = 0
        for i in range(len(arr) - n):

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                j = 1

        if not j:
            break
        n += 1

        print(arr)

    print(arr)
    return arr


array = [random.randint(-100, 99) for i in range(10)]
print(array)
print('-----------')

bubble_sort(array)
print('-----------')
bubble_sort_modified(array)

# Если честно, нашла подсказку в Википедии, до этого не понимала, как можно улучшить, хотя замечала эти лишние
# итерации... И сейчас понятно, что задание элементарное :(
