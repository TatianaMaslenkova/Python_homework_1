# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример: A (3,6); B (2,1) -> 5.09  A (7,-5); B (1,-1) -> 7.21
coordinate_a_x = int(input('Введите координату x точки А: '))
coordinate_a_y = int(input('Введите координату y точки А: '))
coordinate_b_x = int(input('Введите координату x точки B: '))
coordinate_b_y = int(input('Введите координату y точки B: '))
import math
square_difference_x = math.pow(coordinate_b_x - coordinate_a_x, 2)
square_difference_y = math.pow(coordinate_b_y - coordinate_a_y, 2)
distance = math.sqrt(square_difference_x + square_difference_y)
distance = round(distance, 2)
print(f'Расстояние между точками: {distance}')