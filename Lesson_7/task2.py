# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
#  промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr):

    if len(arr) == 1:
        return arr

    elif len(arr) > 1:
        array = [0]*len(arr)
        length = len(arr) // 2

        list_left = arr[:length]
        list_right = arr[length:]

        list_left_sorted = merge_sort(list_left)
        list_right_sorted = merge_sort(list_right)

        i = 0
        j = 0
        k = 0
        while i < len(list_left_sorted) and j < len(list_right_sorted):
            if list_left_sorted[i] < list_right_sorted[j]:
                array[k] = list_left_sorted[i]
                i += 1
            else:
                array[k] = list_right_sorted[j]
                j += 1
            k += 1

        while i < len(list_left_sorted):
            array[k] = list_left_sorted[i]
            i += 1
            k += 1

        while j < len(list_right_sorted):
            array[k] = list_right_sorted[j]
            j += 1
            k += 1

        return array


array = [round(random.uniform(0, 50), 2) for i in range(7)]
print(array)
print(merge_sort(array))
