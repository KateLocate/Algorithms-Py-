# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('Введите две латинские буквы')

a = input('Первая буква:')
b = input('Вторая буква:')
previous_symbols = ord('a') - 1

n1 = ord(a) - previous_symbols
n2 = ord(b) - previous_symbols

if n1 > n2:
    d = n1 - n2 - 1

elif n1 < n2:
    d = n2 - n1 - 1

else:
    d = 0

print(f'Порядковый номер первой буквы:{n1}, второй буквы:{n2}. \nРасстояние между буквами:{d} символов.')