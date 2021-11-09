"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 20

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

oft_numb_cnt = 0
oft_numb = []
for n in array:
    cnt = 0
    for i in array:
        if i == n:
            cnt += 1
    if cnt > oft_numb_cnt:
        oft_numb_cnt = cnt
        oft_numb = [n]
    elif cnt == oft_numb_cnt:
        if n not in oft_numb:
            oft_numb += [n]
numb_prnt = ''
for index, nm in enumerate(oft_numb):
    if index != len(oft_numb) - 1:
        numb_prnt += str(nm) + ', '
    else:
        numb_prnt += str(nm)
print(f'Все числа уникальны в массиве {array}' if oft_numb_cnt == 1
      else f'В массиве: {array}\nЧаще всего встречается число/а {numb_prnt} с повтором {oft_numb_cnt} раз/а')
