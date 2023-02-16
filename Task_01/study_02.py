# list_1 = list() # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз
#  n = int(input()) # пользователь вводит целое число
#  list_1.append(n) # сохранение элемента в конец списка+ lj,добавление числа или буквы
# # 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# # 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# # 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# # 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# # 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
# print(list_1) # [12, 7, -1, 21, 0]

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Метод pop удаляет последний элемент из списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop())  # 0
# print(list_1)  # [12, 7, -1, 21]
# print(list_1.pop())  # 21
# print(list_1)  # [12, 7, -1]
# print(list_1.pop())  # -1
# print(list_1)  # [12, 7]

# word = 'Python'

# for letter in word:
#     print(letter)

# print()
# for i in (0, 1, 2, 3, 4, 5):
#     print(word[i])

# print()
# print(range(len(word)))
# print(list(range(len(word))))
# for i in range(len(word)):
#     print(word[i])


def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)


print(fact(5))
