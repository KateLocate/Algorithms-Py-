# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три сравниваемых числа')

a = int(input('Число 1:'))
b = int(input('Число 2:'))
c = int(input('Число 3:'))

if a > b:
    if a > c:
        if c > b:
            print(f'Среднее по величине число {c}')
        else:
            print(f'Среднее по величине число {b}')
    else:
        print(f'Среднее по величине число {a}')
else:
    if b > c:
        if a > c:
            print(f'Среднее по величине число {a}')
        else:
            print(f'Среднее по величине число {c}')
    else:
        print(f'Среднее по величине число {b}')
