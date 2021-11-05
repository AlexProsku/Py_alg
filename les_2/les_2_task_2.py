"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

Блок-схема доступна по ссылке  https://drive.google.com/file/d/1GeOZGVrZdo2orMYAscSIlUU9di4tbKu2/view?usp=sharing
"""

print('Введите натуральное число')
n = int(input('n = '))
odd_n = 0
even_n = 0
while n != 0:
    last_n = n % 10
    n = n // 10
    if last_n % 2 == 0:
        even_n += 1
    else:
        odd_n += 1
print(f'Количество чётных чисел = {even_n}\n'
      f'Количество нечётных чисел = {odd_n}')
