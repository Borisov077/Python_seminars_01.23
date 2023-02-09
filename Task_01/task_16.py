# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

n = int(input('Введите n: '))

int_arr = [randint(1, n//2+n % 2+1)]
print(f'Массив случайных чисел {n} целых чисел от 1 до {n//2+n%2}')
print(int_arr)

x = int(input("Введите x: "))

print(f'Число {x} встречается в массиве {int_arr.count (x) } раз')