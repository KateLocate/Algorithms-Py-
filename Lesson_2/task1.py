# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые
#  данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
#  и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0
#  в качестве делителя.

print('Введите два числа и операцию("+","-","*","/") или "0" для выхода из калькулятора')

op = ' '

while op != '0':
    n1 = int(input('------------------\nПервое число:'))
    n2 = int(input('Второе число:'))
    op = input('Операция:')
    if op == '+':
        print(f'Ответ: {n1 + n2}')
    elif op == '-':
        print(f'Ответ: {n1 - n2}')
    elif op == '*':
        print(f'Ответ: {n1 * n2}')
    elif op == '/':
        if n2 != 0:
            print(f'Ответ: {n1 / n2}')
        else:
            print('Вы пытаетесь делить на ноль!')
    elif op != '0':
        print('Вы ввели несуществующую операцию, попробуйте снова.')
