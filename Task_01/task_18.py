# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

n = int(input('Введите n: '))

int_arr = [randint(-n//2, n//2+1) for i in range(n)]
print(f'Массив случайных чисел {n} целых чисел от {-n//2} до {n//2}')
print(int_arr)

x = int(input("Введите x: "))
distances = {abs(x-num) for num in int_arr}
min_dist = min(distances)
nearset_numbers = {num for num in int_arr if abs(x-num) == min_dist}
print(f'Числа {nearset_numbers} являются ближайшим к числу {x} числам массива и находятся от него в на расстоянии {min_dist}')
