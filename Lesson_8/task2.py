# 2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

# Здесь должен быть работающий код, но он не работающий :)

from collections import Counter


def haffman_encoding(string):
    symbols_by_value = dict(Counter(string).most_common())

    def tree_generator(symbols):
        pool = []
        tree = []

        for keys, values in symbols.items():
            unit = MyNode(mass=values, left=None, right=None, value=keys)
            pool.append(unit)
            tree.append(unit)

        while len(pool) > 1:
            pool = sorted(pool, key=lambda unit: unit.mass, reverse=True)
            unit = MyNode(mass=(pool[-1].mass + pool[-2].mass), left=pool[-1], right=pool[-2])
            pool.pop()
            pool.pop()
            pool.append(unit)
            tree.append(unit)

        tree = sorted(tree, key=lambda unit: unit.mass, reverse=True)

        return tree

    tree = tree_generator(symbols_by_value)
    items = symbols_by_value.keys()

    # def encoding(tree, symbols):
    #     dic = []
    #
    #     def search(tree_root):
    #
    #         if tree_root.value == 0:
    #             search(tree_root.left)
    #             search(tree_root.right)
    #
    #         else:
    #             print(tree_root.value)
    #             return tree_root.value
    #
    #     search(tree[1])
    #
    #
    #     return dic
    #
    # dic = encoding(tree, items)


class MyNode:

    def __init__(self, mass, left, right, value=0):
        self.mass = mass
        self.left = left
        self.right = right
        self.value = value


s = 'beep boop beer!'
haffman_encoding(s)
