"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10       # размер массива должен быть не меньше двух элементов
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив до изменений: {array}')

min_item, min_item_idx, max_item, max_item_idx = array[0], 0, array[0], 0
for index, item in enumerate(array):
    if min_item >= item:
        min_item = item
        min_item_idx = index
    if max_item <= item:
        max_item = item
        max_item_idx = index
if min_item != max_item:
    array[min_item_idx], array[max_item_idx] = max_item, min_item
    print(f'Массив после изменений: {array}')
else:
    print('Минимальное и максимальное значение у элементов в массиве равны и менять их местами нет смысла!')
