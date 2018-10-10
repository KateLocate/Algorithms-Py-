# Написать два алгоритма нахождения i - го по счёту простого числа. В первом случае использовать алгоритм решето
#  Эратосфена.
# Проанализировать скорость и сложность алгоритмов.

import cProfile


def eratosphen(n):

    sieve = [0, 0]
    values = []
    m = 1
    counter = 0

    while counter <= n:
        m += 1
        sieve.append(m)

        for i in range(2, m):
            if sieve[i] != 0:
                j = i * 2

                while j < m:
                    sieve[j] = 0
                    j += i

        counter = len(sieve) - sieve.count(0)

    for i, item in enumerate(sieve):
        if item != 0:
            values.append(item)

    value = values[-2]

    return value


# Данные по скорости работы eratosphen:

# 2000 loops, best of 5: 149 usec per loop
# 5 loops, best of 5: 52.2 msec per loop - 100
# 1 loop, best of 5: 13.7 sec per loop - 1000

# В моей реализации решета Эратосфена задействовано три вложенных цикла и еще один, реорганизующий полученный набор
# значений. Вкупе все это приводит к катастрофически резкому падению быстродействия.
# Сложность все так же линейная?


def simple_number(index):

    n = [1]
    values = [0, 2]

    while len(values) <= index:
        sign = 0

        n.append(n[-1] + 2)
        values.append(n[-1])

        for j in range(1, len(values)):

            if values[-1] % values[j] == 0 and values[-1] != values[j]:
                sign = 1

        if sign:
            values.remove(values[-1])

    return values[-1]


# Данные по скорости работы simple_number:

# 10000 loops, best of 5: 36.8 usec per loop - 10
# 100 loops, best of 5: 2.95 msec per loop - 100
# 1 loop, best of 5: 426 msec per loop - 1000

# В этой функции удалось обойтись одним циклом, что обуславливает меньшиие потери в скорости при увеличении N.
# Сложность все так же линейная?
