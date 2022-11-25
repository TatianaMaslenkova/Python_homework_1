# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример: x=34; y=-30 -> 4  x=2; y=4-> 1  x=-34; y=-30 -> 3
coordinate_x = int(input('Введите координату x: '))
coordinate_y = int(input('Введите координату y: '))
if coordinate_x > 0 and coordinate_y > 0:
    print('1 четверть')
elif coordinate_x < 0 and coordinate_y > 0:
    print('2 четверть')
elif coordinate_x < 0 and coordinate_y < 0:
    print('3 четверть')
elif coordinate_x > 0 and coordinate_y < 0:
    print('4 четверть')
else:
    print('Точка лежит на одной из осей')