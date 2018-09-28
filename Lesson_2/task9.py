# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
#  его цифр.

print('Введите произвольное количество чисел. Чтобы закончить сравнение, введите "0"')

n = 1
m = 1
maximum = 0
summa = 0

while n != 0:
    n = int(input(f'Число {m}:'))
    previous = 0
    number = n

    if number >= 0:
        m += 1
        while number > 0:
            next = number % 10
            summa = previous + next
            previous += next
            number = number // 10

        if summa > maximum:
            maximum = summa

    else:
        print('Введите число большее или равное нулю.')

print(f'Максимальное число: {maximum}')
