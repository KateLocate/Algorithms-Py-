# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. Например,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке. Для
#  решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

import hashlib

s = input('Введите строку для вычисления количества подстрок:')


def strings_in_string(string):

    string_hash = hashlib.sha1(string.encode('utf-8')).hexdigest()
    hash_list = []

    for j in range(len(string)):

        for i in range(j+1, len(string)+1):
            substring_hash = hashlib.sha1(string[j:i].encode('utf-8')).hexdigest()

            if substring_hash != string_hash and substring_hash not in hash_list:
                hash_list.append(substring_hash)

    return len(hash_list)


print(strings_in_string(s))
