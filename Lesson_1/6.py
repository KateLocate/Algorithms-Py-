# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input('Введите номер буквы в латинском алфавите:'))
previous_symbols = ord('a') - 1
last_number = 26

if 0 < n <= last_number:
    s = chr(n + previous_symbols)
    print(f'Искомая буква:{s}')

else:
    print('Максимальное число - 26, минимальное - 1.')