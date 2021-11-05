"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

Блок-схема доступна по ссылке  https://drive.google.com/file/d/1GeOZGVrZdo2orMYAscSIlUU9di4tbKu2/view?usp=sharing
"""


def sum_n(num, s=0):
    if num == 0:
        return s
    else:
        s += num % 10
        num //= 10
        return sum_n(num, s)


print('Вводите натуральные числа через Enter. Для завершения ввода - введите 0 и Enter')
max_n = 0
max_n_sum = 0
while True:
    n = int(input('Натуральное число: '))
    if n == 0:
        print(f'Наибольшее по сумме цифр натуральное число = {max_n},\n'
              f'сумма его цифр = {max_n_sum}')
        break
    sum_nn = sum_n(n)
    if sum_nn > max_n_sum:
        max_n_sum = sum_nn
        max_n = n
