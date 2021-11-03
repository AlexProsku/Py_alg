# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

# Блок-схема доступна по ссылке https://drive.google.com/file/d/1ioprat_Dsmrm48Bi3u4yqFX7J9m0WGq5/view?usp=sharing

print('Введите координаты точки A (x1, y1)')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
print('Введите координаты точки B (x2, y2)')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
if x1 == x2:
    print(f'x = {x1:.2f}')
elif y1 == y2:
    print(f'y = {y1:.2f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.2f} * x + {b:.2f}')
