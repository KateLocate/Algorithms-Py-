# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

print('Введите начало и конец диапазона (числа, символы алфавита (латинского))')

a = input('Начало:')
b = input('Конец:')

symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']

if a in symbols and b in symbols:
    start = symbols.index(a)
    stop = symbols.index(b)
    cut = symbols[start:stop]
    symbol = random.choice(cut)
    print(f'Случайный символ:{symbol}')

elif a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    symbol = random.randint(a, b)
    print(f'Случайное целое число:{symbol}')

elif '.' in a and '.' in b:
    a = float(a)
    b = float(b)
    symbol = random.uniform(a, b)
    print(f'Случайное вещественное число:{symbol}')

else:
    print('Ошибка!')
