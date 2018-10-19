# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
#  промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random


def bubble_sort(array):
    arr = array[:]
    n = 1

    while n < len(arr):

        for i in range(len(arr) - n):

            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        n += 1

    return arr


def bubble_sort_modified(array):
    arr = array[:]
    n = 1

    while n < len(arr):
        is_sorted = False

        for i in range(len(arr) - n):

            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = True

        if not is_sorted:
            break
        n += 1

    return arr


array = [random.randint(-100, 99) for i in range(10)]
print(array)
print('-----------')

print(bubble_sort(array))
print('-----------')
print(bubble_sort_modified(array))
