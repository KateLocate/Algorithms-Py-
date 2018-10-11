# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
#  массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

print('Программа для получения суммы и произведения чисел в шестнадцатеричной системе счисления.')

while True:
    a = deque(input('Введите первое число:').upper(), maxlen=10)
    b = deque(input('Введите второе число:').upper(), maxlen=10)
    c = input('Введите знак операции (* или +) или "N" для выхода :')

    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}

    dict_invert = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                   12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    summa = deque([0]*20, maxlen=20)
    mult = deque([0]*20, maxlen=20)

    s_current_add = 0
    mult_current_add = 0

    if c == '+':
        if len(a) < len(b):

            while len(a) < len(b):
                a.appendleft('0')

        elif len(b) < len(a):

            while len(b) < len(a):
                b.appendleft('0')

        for i in range(-1, -(len(a) + 1), -1):

            if a[i] in dict:
                s_current = (dict[a[i]] + dict[b[i]]) % 16
                s_next = (dict[a[i]] + dict[b[i]]) // 16

                if s_next > 0:
                    summa[i-1] += s_next

                summa[i] += s_current
                summa[i] += s_current_add
                s_current_add = 0

                if summa[i] >= 16:
                    s_current_add += summa[i] // 16
                    summa[i] = summa[i] % 16

            else:
                print('Вы ввели не шестнадцатеричное число. Попробуйте снова:')
                break

        while summa[0] == 0:
            summa.popleft()

        for i in range(len(summa)):
            summa[i] = dict_invert.get(summa[i])

        s_list = list(summa)

        print(f'Сумма: {s_list}\n')

    # elif c == '*':
    #     index = len(mult)
    #
    #     for i in range(-1, -(len(a) + 1), -1):
    #
    #         if a[i] in dict:
    #
    #             for j in range(-1, -(len(b) + 1), -1):
    #                 mult_current = (dict[a[i]] * dict[b[j]]) % 16
    #                 mult_next = (dict[a[i]] * dict[b[j]]) // 16
    #
    #                 m = [0]*len(mult)
    #                 m[index-1] += mult_next
    #
    #                 m[index] += mult_current
    #                 m[index] += mult_current_add
    #                 mult_current_add = 0
    #
    #                 while m[index] >= 16:
    #                     mult_current_add += m[index] // 16
    #                     m[index] -= mult_current_add
    #                     print(m[index])
    #                     index -= 1
    #                 print(mult, m, mult_next, mult_current_add)
    #                 mult = m
    #                 mult.append(0)
    #             index -= 1
    #
    #         else:
    #             print('Вы ввели не шестнадцатеричное число. Попробуйте снова:')
    #             break
    #
    #     while mult[0] == 0:
    #         mult.popleft()
    #
    #     print(mult)
    #
    #     for i in range(len(mult)):
    #         mult[i] = dict_invert.get(mult[i])
    #
    #     mult_list = list(mult)
    #
    #     print(f'Произведение: {str(mult_list)}')

    elif c == "N":
        break

    else:
        print('Ошибка при вводе знака оператора или ключа для выхода.\n')
