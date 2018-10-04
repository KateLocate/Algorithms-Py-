# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

numbers = [i for i in range(2, 100)]
divider = 2

print('Среди чисел от 2 до 99: \n')

while divider <= 9:
    counter = 0

    for i, item in enumerate(numbers):

        if item % divider == 0:
            counter += 1

    print(f'{counter} кратны {divider}')

    divider += 1
