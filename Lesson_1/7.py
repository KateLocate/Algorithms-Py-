# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
#  составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
#  равнобедренным или равносторонним.

print('Введите длины сторон треугольника')

a = float(input('Сторона 1:'))
b = float(input('Сторона 2:'))
c = float(input('Сторона 3:'))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Треугольник равносторонний.')
    elif a != b and b != c and a != c:
        print('Треугольник разносторонний.')
    else:
        print('Треугольник равнобедренный.')
else:
    print('Треугольник не существует.')
