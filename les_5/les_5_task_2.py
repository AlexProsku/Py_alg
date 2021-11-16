"""
2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их
как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

number_1 = input('Введите первое слагаемое: ')
# number_1 = 'ff4aeF20'
num_1 = list(number_1.upper())
number_2 = input('Введите второе слагаемое: ')
# number_2 = 'f4a00a7010'
num_2 = list(number_2.upper())
# print(f'{number_1}+{number_2}')

d_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
result = deque([])
tmp_n = 0
tmp_n_1 = 0
tmp_n_2 = 0
for i in range((max(len(num_1), len(num_2)) + 1)):
    if len(num_1) != 0:
        tmp_n_1 = d_16.index(num_1.pop())
    else:
        tmp_n_1 = 0
    if len(num_2) != 0:
        tmp_n_2 = d_16.index(num_2.pop())
    else:
        tmp_n_2 = 0
    sum_ = tmp_n_1 + tmp_n_2
    if sum_ + tmp_n < 16:
        result.appendleft(d_16[sum_ + tmp_n])
        tmp_n = 0
    else:
        result.appendleft(d_16[sum_ + tmp_n - 16])
        tmp_n = 1
if result[0] == '0':
    result.popleft()

print(f'{list(number_1.upper())}\n + \n{list(number_2.upper())}\n = \n{list(result)}')
