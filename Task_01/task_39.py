# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# from module import creat_list

n = int(input('Введите колличество элементов последовательности число N: '))
m = int(input('Введите колличество элементов последовательности число M: '))
n_list = creat_list(n)
m_list = creat_list(m)
z_list = []
for i in range(n):
    if n_list[i] not in m_list:
        z_list.append(n_list[i])
print(*n_list)
print(*m_list)

print(*z_list)
