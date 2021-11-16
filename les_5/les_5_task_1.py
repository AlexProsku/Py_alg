"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter

c_profit = Counter()
n_c = int(input("Введите количество предприятий: "))
for i in range(n_c):
    c_name = input(f"Введите наименование предприятия № {i + 1}: ")
    for k in range(4):
        c_profit += Counter({c_name: float(input(f"Введите прибыль предприятия № {i + 1} за квартал {k + 1}: "))})

avg_profit = sum(c_profit.values()) / n_c
high_c = []
low_c = []
print(f'Средняя прибыль за год по компаниям = {avg_profit: .2f}')
for i in c_profit:
    if c_profit.get(i) > avg_profit:
        high_c.append(i)
    elif c_profit.get(i) < avg_profit:
        low_c.append(i)
print(f'Предприятия с прибылью выше среднего: {", ".join(high_c)}')
print(f'Предприятия с прибылью ниже среднего: {", ".join(low_c)}')
