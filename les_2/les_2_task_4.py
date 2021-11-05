"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.

Блок-схема доступна по ссылке  https://drive.google.com/file/d/1GeOZGVrZdo2orMYAscSIlUU9di4tbKu2/view?usp=sharing
"""


def sum_n(num, s=1, n_line=1):
    if num == 1:      # полагаем, что у нас идеальный пользователь и вводил натуральное число
        return s
    else:
        n_line /= -2
        s += n_line
        num -= 1
        return sum_n(num, s, n_line)


print('Введите количество элементов')
n = int(input('n = '))
print(f'Сумма = {sum_n(n)}')
