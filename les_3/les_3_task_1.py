"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

MIN_RANGE = 2
MAX_RANGE = 99
MIN_MULTIPLE = 2
MAX_MULTIPLE = 9

range_lst = list(range(MIN_RANGE, MAX_RANGE + 1))
multiple_lst = list(range(MIN_MULTIPLE, MAX_MULTIPLE + 1))

for m in multiple_lst:
    count_ = 0
    for r in range_lst:
        if r % m == 0:      # не добавлял условия деления на ноль, т.к. у нас идеальный пользователь
            count_ += 1
    print(f'Числу {m} кратно {count_} чисел из диапазона')
