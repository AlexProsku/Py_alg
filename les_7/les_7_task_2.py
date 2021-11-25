"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random


def sort_array(array):
    l_el = 0
    r_el = 0

    if len(array) <= 1:
        return array

    l_array = sort_array(array[:len(array) // 2])
    r_array = sort_array(array[len(array) // 2:])

    while len(l_array) > l_el and len(r_array) > r_el:
        if l_array[l_el] < r_array[r_el]:
            array[l_el + r_el] = l_array[l_el]
            l_el += 1
        else:
            array[l_el + r_el] = r_array[r_el]
            r_el += 1

    while len(l_array) > l_el:
        array[l_el + r_el] = l_array[l_el]
        l_el += 1
    while len(r_array) > r_el:
        array[l_el + r_el] = r_array[r_el]
        r_el += 1

    return array


SIZE = 9
MIN_ITEM = 0
MAX_ITEM = 50
FRACT = 2    # число знаков после дапятой - условно берём 2
rand_array = [random.randrange(MIN_ITEM * 10 ** FRACT, MAX_ITEM * 10 ** FRACT) / 10 ** FRACT for _ in range(SIZE)]

print(f'Исходный массив: {rand_array}')
print(f'Массив после сортировки: {sort_array(rand_array)}')
