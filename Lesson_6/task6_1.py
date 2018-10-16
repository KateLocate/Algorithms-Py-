import sys


def show_total_size(*z):

        total_size = 0

        def show_size(x, level=0):

            print('\t' * level, f'type = {x.__class__}, size={sys.getsizeof(x)}, object = {x}')

            if hasattr(x, '__iter__'):

                if hasattr(x, 'items'):
                    for y in x.items():
                        show_size(y, level + 1)

                elif not isinstance(x, str):

                    for y in x:
                        show_size(y, level + 1)

        for x, item in enumerate(z):
            show_size(item)
            total_size += sys.getsizeof(item)

        print(f'Размер всех объектов: {total_size}')

# Разрядность системы - 64б, версия ОС - Windows7
