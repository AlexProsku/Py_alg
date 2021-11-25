"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.
"""

import random


def median_array(array):
    for i in array:
        left, right, current = 0, 0, 0
        for j in array:
            if i < j:
                right += 1
            elif i > j:
                left += 1
            else:
                current += 1
        if right == left or left + current - 1 == right or left == right + current - 1:
            return i
    return f'Массив не отвечает условию 2n+1'


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
rand_array = [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(2 * SIZE + 1)]

print(f'Исходный массив: {rand_array}')
print(f'Медиана = {median_array(rand_array)}')
