"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
import cProfile
import timeit

"""
Выбрал задачу 1 из урока 3:
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def frqnc_1(min_range, max_range, min_multiple, max_multiple):
    range_lst = list(range(min_range, max_range + 1))
    multiple_lst = list(range(min_multiple, max_multiple + 1))
    print_ = ''
    for m in multiple_lst:
        count_ = 0
        for r in range_lst:
            if r % m == 0:
                count_ += 1
        print_ += f'Числу {m} кратно {count_} число/ла/ел из диапазона {min_range} - {max_range}\n'
    return print_


def frqnc_2(min_range, max_range, min_multiple, max_multiple):
    range_lst = list(range(min_range, max_range + 1))
    multiple_lst = list(range(min_multiple, max_multiple + 1))

    def c_frqnc_1():
        print_ = ''
        for m in multiple_lst:
            def c2_frqnc_1():
                count_ = 0
                for r in range_lst:
                    if r % m == 0:
                        count_ += 1
                return f'Числу {m} кратно {count_} число/ла/ел из диапазона {min_range} - {max_range}\n'
            print_ += c2_frqnc_1()
        return print_
    return c_frqnc_1()


def frqnc_3(min_range, max_range, min_multiple, max_multiple):
    print_ = ''
    for m in range(min_multiple, max_multiple + 1):
        count_ = 0
        for r in range(min_range, max_range + 1):
            if r % m == 0:
                count_ += 1
        print_ += f'Числу {m} кратно {count_} число/ла/ел из диапазона {min_range} - {max_range}\n'
    return print_


def frqnc_4(min_range, max_range, min_multiple, max_multiple):
    print_ = ''
    num_multiple = min_multiple
    while num_multiple <= max_multiple:
        count_ = 0
        num_range = min_range
        while num_range <= max_range:
            if num_range % num_multiple == 0:
                count_ += 1
            num_range += 1
        print_ += f'Числу {num_multiple} кратно {count_} число/ла/ел из диапазона {min_range} - {max_range}\n'
        num_multiple += 1
    return print_


# print(frqnc_1(2, 99, 2, 9))   # для отладки (проверить, что функция возвращает верный результат)
# print(frqnc_2(2, 99, 2, 9))   # для отладки (проверить, что функция возвращает верный результат)
# print(frqnc_3(2, 99, 2, 9))   # для отладки (проверить, что функция возвращает верный результат)
# print(frqnc_4(2, 99, 2, 9))   # для отладки (проверить, что функция возвращает верный результат)

print(timeit.timeit('frqnc_1(2, 99, 2, 9)', number=100, globals=globals()))     # 0.003223
print(timeit.timeit('frqnc_1(2, 990, 2, 9)', number=100, globals=globals()))    # 0.0279609
print(timeit.timeit('frqnc_1(2, 9900, 2, 9)', number=100, globals=globals()))   # 0.28491429999999995
print(timeit.timeit('frqnc_1(2, 99000, 2, 9)', number=100, globals=globals()))  # 2.8798934999999997

cProfile.run('frqnc_1(2, 9900, 2, 9)')
"""
         4 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.003    0.003    0.003    0.003 les_4_task_1.py:20(frqnc_1)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('frqnc_1(2, 99000, 2, 9)')
"""
         4 function calls in 0.030 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.030    0.030 <string>:1(<module>)
        1    0.029    0.029    0.029    0.029 les_4_task_1.py:20(frqnc_1)
        1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print(timeit.timeit('frqnc_2(2, 99, 2, 9)', number=100, globals=globals()))       # 0.0033775000000000333
print(timeit.timeit('frqnc_2(2, 990, 2, 9)', number=100, globals=globals()))      # 0.028190599999999844
print(timeit.timeit('frqnc_2(2, 9900, 2, 9)', number=100, globals=globals()))     # 0.30258569999999985
print(timeit.timeit('frqnc_2(2, 99000, 2, 9)', number=100, globals=globals()))    # 3.0650779

cProfile.run('frqnc_2(2, 9900, 2, 9)')
"""
         13 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 les_4_task_1.py:33(frqnc_2)
        1    0.000    0.000    0.003    0.003 les_4_task_1.py:36(c_frqnc_1)
        8    0.003    0.000    0.003    0.000 les_4_task_1.py:39(c2_frqnc_1)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('frqnc_2(2, 99000, 2, 9)')
"""
         13 function calls in 0.030 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.030    0.030 <string>:1(<module>)
        1    0.001    0.001    0.030    0.030 les_4_task_1.py:33(frqnc_2)
        1    0.000    0.000    0.028    0.028 les_4_task_1.py:36(c_frqnc_1)
        8    0.028    0.004    0.028    0.004 les_4_task_1.py:39(c2_frqnc_1)
        1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print(timeit.timeit('frqnc_3(2, 99, 2, 9)', number=100, globals=globals()))       # 0.003249199999999952
print(timeit.timeit('frqnc_3(2, 990, 2, 9)', number=100, globals=globals()))      # 0.032638600000000295
print(timeit.timeit('frqnc_3(2, 9900, 2, 9)', number=100, globals=globals()))     # 0.3501674999999995
print(timeit.timeit('frqnc_3(2, 99000, 2, 9)', number=100, globals=globals()))    # 3.4491732000000006

cProfile.run('frqnc_3(2, 9900, 2, 9)')
"""
         4 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.003    0.003    0.003    0.003 les_4_task_1.py:50(frqnc_3)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('frqnc_3(2, 99000, 2, 9)')
"""
         4 function calls in 0.032 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.032    0.032 <string>:1(<module>)
        1    0.032    0.032    0.032    0.032 les_4_task_1.py:50(frqnc_3)
        1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print(timeit.timeit('frqnc_4(2, 99, 2, 9)', number=100, globals=globals()))       # 0.0049637000000011255
print(timeit.timeit('frqnc_4(2, 990, 2, 9)', number=100, globals=globals()))      # 0.0498144000000007
print(timeit.timeit('frqnc_4(2, 9900, 2, 9)', number=100, globals=globals()))     # 0.5152889999999992
print(timeit.timeit('frqnc_4(2, 99000, 2, 9)', number=100, globals=globals()))    # 5.175565300000001

cProfile.run('frqnc_4(2, 9900, 2, 9)')
"""
         4 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.005    0.005    0.005    0.005 les_4_task_1.py:61(frqnc_4)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('frqnc_4(2, 99000, 2, 9)')
"""
         4 function calls in 0.057 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.057    0.057 <string>:1(<module>)
        1    0.057    0.057    0.057    0.057 les_4_task_1.py:61(frqnc_4)
        1    0.000    0.000    0.057    0.057 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Замеры проводил путём изменения верхней границы диапазона натуральных чисел (с 99 на 990, 9900, 99000)
ВЫВОД:
Во всех примерах прослеживается линейная сложность O(n) - проход по элементам массива. Это косвенно доказывают замеры
timeit, т.е. при увеличении набора входных данных (массива) время выполнения пропорционально увеличивается.
Изначально реализованный вариант с функцией frqnc_1, которая использует 2 вложенных цикла для перебора двух 
сгенерированных списков - оказался самым оптимальным.
Второй вариант frqnc_2 искусственно разбитый на функции с вызовом цикла функций оказался немного медленным (предполагаю,
что из-за вызова функций). Зато с помощью cProfile получил детализацию слабого места с многократным вызовом функции.
Третий вариант frqnc_3 с использованием функции range для итерации цикла оказался медленее двух предыдущих вариантов с 
перебором значений из списка (хотя изначально на него были надежды).
А последний вариант frqnc_4 с циклом while, как и предполагал, оказался самым медленным.
"""
