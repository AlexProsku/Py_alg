"""
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
"""

import timeit
import cProfile


def sieve_er(numb):     # Решето Эратосфена
    res = [2]
    n = 3
    while len(res) < numb:
        sieve = [i for i in range(n)]
        sieve[1] = 0
        for i in range(2, n):
            if sieve[i] != 0:
                j = i + i
                while j < n:
                    sieve[j] = 0
                    j += i
        res = [i for i in sieve if i != 0]
        n += n
    return res[numb - 1]


def sieve_cl(numb):     # Классический способ проверки
    cntr = 1
    n = 3
    smpl_n = 2
    while cntr < numb:
        smpl = True
        for i in range(2, n):
            if n % i == 0:
                smpl = False
                break
        if smpl is True:
            cntr += 1
            smpl_n = n
        n += 1
    return smpl_n


# print(sieve_er(7))    # для отладки (проверить, что функция возвращает 17)
# print(sieve_cl(7))   # для отладки (проверить, что функция возвращает 17)

print(timeit.timeit('sieve_er(10)', number=100, globals=globals()))     # 0.0013878999999999975
print(timeit.timeit('sieve_er(100)', number=100, globals=globals()))    # 0.0263086
print(timeit.timeit('sieve_er(1000)', number=100, globals=globals()))   # 0.4831891
print(timeit.timeit('sieve_er(10000)', number=100, globals=globals()))  # 9.3584278

cProfile.run('sieve_er(1000)')
"""
         44 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.004    0.004    0.005    0.005 les_4_task_2.py:27(sieve_er)
       13    0.001    0.000    0.001    0.000 les_4_task_2.py:31(<listcomp>)
       13    0.000    0.000    0.000    0.000 les_4_task_2.py:39(<listcomp>)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
       14    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('sieve_er(10000)')
"""
         56 function calls in 0.093 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.093    0.093 <string>:1(<module>)
        1    0.073    0.073    0.092    0.092 les_4_task_2.py:27(sieve_er)
       17    0.011    0.001    0.011    0.001 les_4_task_2.py:31(<listcomp>)
       17    0.008    0.000    0.008    0.000 les_4_task_2.py:39(<listcomp>)
        1    0.000    0.000    0.093    0.093 {built-in method builtins.exec}
       18    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print(timeit.timeit('sieve_cl(10)', number=100, globals=globals()))     # 0.0009345000000013926
print(timeit.timeit('sieve_cl(100)', number=100, globals=globals()))    # 0.08632679999999837
print(timeit.timeit('sieve_cl(1000)', number=100, globals=globals()))   # 14.0324671
# print(timeit.timeit('sieve_cl(10000)', number=100, globals=globals()))  # долго не дождался

cProfile.run('sieve_cl(1000)')
"""
         4 function calls in 0.138 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.138    0.138 <string>:1(<module>)
        1    0.138    0.138    0.138    0.138 les_4_task_2.py:44(sieve_cl)
        1    0.000    0.000    0.138    0.138 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('sieve_cl(10000)')
"""
         4 function calls in 18.924 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   18.924   18.924 <string>:1(<module>)
        1   18.924   18.924   18.924   18.924 les_4_task_2.py:44(sieve_cl)
        1    0.000    0.000   18.924   18.924 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
ВЫВОД:
Функция с решетом Эратосфена оказалась более оптимальной реализацией.
Очень интересный результат показал cProfile в решете - многокрытный вызов
"""
