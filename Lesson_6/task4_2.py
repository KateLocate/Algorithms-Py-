# Написать два алгоритма нахождения i - го по счёту простого числа. В первом случае использовать алгоритм решето
# Эратосфена.
# Проанализировать скорость и сложность алгоритмов.

import cProfile
import task6_1 as t


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

    t.show_total_size(n, values, m, counter, j)

    return value


# Данные по скорости работы eratosphen:

# 2000 loops, best of 5: 149 usec per loop
# 5 loops, best of 5: 52.2 msec per loop - 100
# 1 loop, best of 5: 13.7 sec per loop - 1000

# Размер всех объектов: 304 eratosphen(10)
# Размер всех объектов: 1024 (100)
# Размер всех объектов: 9136 (1000)


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

    t.show_total_size(n, values, sign)

    return values[-1]


# Данные по скорости работы simple_number:

# 10000 loops, best of 5: 36.8 usec per loop - 10
# 100 loops, best of 5: 2.95 msec per loop - 100
# 1 loop, best of 5: 426 msec per loop - 1000

# Размер всех объектов: 432 simple_number(10)
# Размер всех объектов: 3216 (100)
# Размер всех объектов: 42848 (1000)
# Размер всех объектов: 546680 (10000)

t.show_total_size(simple_number(1000))

#  Здесь очень четкая зависимость скорость - объем памяти: более быстрая вторая реализация, но она же поглощает больше
#  всего памяти, хотя в ней функцией t.show_total_size() мы обрабатываем даже меньше объектов(списки и переменные),
#  чем в решете Эратосфена(и несмотря на то, что я его наполняю :) ). Для 1000 элементов eratosphen задействует
#  уже в пять раз меньше памяти, чем simple_numbers.

#  Что интересно, вторая реализация все равно более дееспособная, так как несмотря на затраты памяти
# (1000-ый элемент - 41Кб, 10 000-ый элемент - 0,5 Мб), время работы остается хоть в каких-то рамках приличия)) Этого
#  нельзя сказать об eratosphen, 10 000-ый элемент я дождаться не смогла...

