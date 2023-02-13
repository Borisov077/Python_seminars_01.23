# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

# def change_marks (n):
#     for i in range(n):

my_list = [randint(1, 5) for _ in range(randint(3, 7))]
print(my_list)

max_elem = max(my_list)
min_elev = min(my_list)

for i in range(len(my_list)):
    if my_list[i] == max_elem:
        my_list[i] = min_elev
print(my_list)
