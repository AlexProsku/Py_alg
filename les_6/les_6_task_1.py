"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Для  анализа взял задачу 4 из урока 3. Определить, какое число в массиве встречается чаще всего.
"""

import random
from sys import getsizeof
from collections import Counter


def calc_mem(*obj_f):
    # Обёртка для создания множества obj_id и передачу служебных атрибутов iter_r, mem_sum
    # В функцию передавать только locals()
    obj_id = set()

    def calc_mem_r(iter_r=0, mem_sum=0, *objects):  # рекурсивная функция подсчёта памяти из словаря locals
        obj_out = []
        simple_obj = True
        iter_r += 1  # номер итерации рекурсивной функции
        objects = objects[0]    # чтобы не считать служебную облочку атрибута (кортеж или список)
        for obj in objects:
            if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
                if id(obj) not in obj_id:
                    mem_sum += getsizeof(obj)
                    obj_id.add(id(obj))
            elif hasattr(obj, '__iter__'):
                if hasattr(obj, 'items'):
                    if id(obj) not in obj_id:
                        if iter_r != 1:     # не считаем оболочку служебного словаря locals
                            mem_sum += getsizeof(obj)
                            obj_id.add(id(obj))
                        for key, value in obj.items():
                            if iter_r == 1:
                                if key.startswith('__'):     # убираем ненужные атрибуты при разборе locals
                                    continue
                            if id(key) not in obj_id:
                                mem_sum += getsizeof(key)
                                obj_id.add(id(key))
                            if id(value) not in obj_id:
                                obj_out.append(value)
                                simple_obj = False
                else:
                    if id(obj) not in obj_id:
                        mem_sum += getsizeof(obj)
                        obj_id.add(id(obj))
                        for i in obj:
                            if id(i) not in obj_id:
                                obj_out.append(i)
                                simple_obj = False
        if simple_obj is True:
            return mem_sum      # Если все элементы распакованы (простые), то завершаем рекурсию
        else:
            return calc_mem_r(iter_r, mem_sum, obj_out)

    return calc_mem_r(0, 0, obj_f)      # Вызываем замер


def exampl_1(array):     # ранее реализованный пример (из домашки)
    # Для чистоты эксперимента вынес генерацию случайного массива во внешку
    # (чтобы для всех примеров были одинаковые входные данные)
    # SIZE = 100
    # MIN_ITEM = 0
    # MAX_ITEM = 20
    # array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

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
    return calc_mem(locals())   # используем для калькуляции памяти переменных


def exampl_2(array):
    cnt_l = Counter()
    for elem in array:
        cnt_l[elem] += 1
    oft_numb = []
    for i in cnt_l.most_common():
        if i[1] == cnt_l.most_common(1)[0][1]:
            oft_numb.append(i[0])
        else:
            break
    print(f'Все числа уникальны в массиве {array}' if cnt_l.most_common(1)[0][1] == 1
          else f'В массиве: {array}\nЧаще всего встречается число/а {", ".join(map(str, oft_numb))} '
               f'с повтором {cnt_l.most_common(1)[0][1]} раз/а')

    return calc_mem(locals())   # используем для калькуляции памяти переменных


def exampl_3(array):
    uniq_el = set(array)
    cnt_numb = 0
    num_max_cnt = ''
    for un_el in uniq_el:
        if array.count(un_el) > cnt_numb:
            num_max_cnt = f'{un_el}'
            cnt_numb = array.count(un_el)
        elif array.count(un_el) == cnt_numb:
            num_max_cnt += f', {un_el}'

    print(f'Все числа уникальны в массиве {array}' if cnt_numb == 1
          else f'В массиве: {array}\nЧаще всего встречается число/а {num_max_cnt} '
               f'с повтором {cnt_numb} раз/а')

    return calc_mem(locals())   # используем для калькуляции памяти переменных


SIZE = 50
MIN_ITEM = 100
MAX_ITEM = 200
array_g = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'В первой реализации под переменные было выделено памяти: {exampl_1(array_g)}')      # 2205
print(f'Во второй реализации под переменные было выделено памяти: {exampl_2(array_g)}')     # 3140
print(f'В третьей реализации под переменные было выделено памяти: {exampl_3(array_g)}')     # 4087

"""
Вывод:
Первая реализация оказалась самой оптимальной по размеру занимаемой памяти переменными.
Самая прожорливая реализация с использованием множества (третий вариант).
Реализация с использованием Counter (второй вариант) оказалась посередине.

OS: Windows 10.0.17763 64-bit

Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]

Random сгенерил массив:
[100, 126, 190, 175, 121, 103, 126, 199, 185, 125, 121, 141, 181, 103, 160, 129, 131, 180, 167, 184, 175, 101, 101, 
184, 165, 129, 123, 157, 139, 131, 146, 167, 193, 170, 103, 198, 198, 192, 129, 154, 164, 175, 147, 138, 152, 151, 157, 
109, 138, 133]
"""
