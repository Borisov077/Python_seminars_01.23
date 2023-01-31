# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import os
os.system('cls')

a = int(input("Количество учеников в 1 классе: "))
b = int(input("Количество учеников в 2 классе: "))
c = int(input("Количество учеников в 3 классе: "))


def Tables(a):
    return a//2+a % 2
print("Количество парт для покупки", Tables(a) + Tables(b) + Tables(c))

classes = []
for i in range(3):
    students = int(input(f'Введите количество учеников в {i + 1} классе: '))
    classes.append(students)

total_desks = 0

for c in classes:
    total_desks += c // 2 + c % 2

print(f'Минимальное количество парт: {total_desks}')