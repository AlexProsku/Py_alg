"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

import random


def sort_array(array):
    for _ in range(len(array)):
        sorted_el = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted_el = False
        if sorted_el:
            return array
    return array


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
rand_array = [random.randint(MIN_ITEM, MAX_ITEM-1) for _ in range(SIZE)]

print(f'Исходный массив: {rand_array}')
print(f'Массив после сортировки: {sort_array(rand_array)}')
