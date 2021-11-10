"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

SIZE = 10       # размер массива должен быть не меньше двух элементов
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_neg_item, max_neg_item_idx = 0, 0

for index, item in enumerate(array):
    if item < 0:
        if max_neg_item == 0:
            max_neg_item = item
            max_neg_item_idx = index
        elif max_neg_item < item:
            max_neg_item = item
            max_neg_item_idx = index
print(f'В массиве: {array}\n'
      f'Максимальный отрицательный элемент = {max_neg_item}, его индекс в массиве = {max_neg_item_idx}')
