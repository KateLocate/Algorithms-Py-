# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

from collections import namedtuple


def company_data():

    name = input('\nВведите имя компании:')
    q_1 = float(input('Прибыль за 1 квартал без указания валюты:'))
    q_2 = float(input('Прибыль за 2 квартал без указания валюты:'))
    q_3 = float(input('Прибыль за 3 квартал без указания валюты:'))
    q_4 = float(input('Прибыль за 4 квартал без указания валюты:'))
    summa = q_1 + q_2 + q_3 + q_4

    data = [name, q_1, q_2, q_3, q_4, summa]

    return data


n = int(input('Введите количество сравниваемых компаний:'))

companies = []
Company = namedtuple('Company', 'name q_1 q_2 q_3 q_4 summa')
average_profit = 0

for i in range(n):
    c = Company._make(company_data())
    companies.append(c)
    average_profit += companies[i].summa / n

more = []
less = []

for i in range(n):

    if companies[i].summa >= average_profit:
        more.append(companies[i].name)

    else:
        less.append(companies[i].name)

print('\nСписок компаний\n')

print('Доход выше среднего:')
for i in range(len(more)):
    print(more[i])

print('Доход ниже среднего:')
for i in range(len(less)):
    print(less[i])
