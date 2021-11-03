# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# Блок-схема доступна по ссылке https://drive.google.com/file/d/1ioprat_Dsmrm48Bi3u4yqFX7J9m0WGq5/view?usp=sharing

first_ltr = ord('a')    # определяем символ первой буквы
print('Введите номер буквы в алфавите в пределах 1-26')
n = int(input('Номер буквы = '))
ltr = chr(first_ltr + n - 1)
print(f'Буква = {ltr}')
