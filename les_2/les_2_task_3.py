"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
если введено число 3486, надо вывести 6843.

Блок-схема доступна по ссылке  https://drive.google.com/file/d/1GeOZGVrZdo2orMYAscSIlUU9di4tbKu2/view?usp=sharing
"""


def rvrs(n, res=0):
    if n == 0:
        return res
    else:
        res = res * 10 + n % 10     # последнюю цифру из n добавляем к res
        n = n // 10
        return rvrs(n, res)


print('Введите натуральное число!')
num = int(input('num = '))
print(f'Развёрнутое число = {rvrs(num)}')
