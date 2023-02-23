# a = 5.8999
# b = 6.9893
# print(round(a+b, 3)) # round - округление после запятой

# print("Введите первое число: ")
# a = int(input())
# print("Введите второе число: ")
# b = int(input())

# print(a, "//", b, "=", a % b)

# Приоритет арифметических операций
# 1. Возведение в степень (**)
# 2. Умножение (*)
# 3. Деление (/)
# 4. Целочисленное деление (//)
# 5. Остаток от деления (%)
# 6. Сложение (+)
# 7. Вычитание (-)


# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5
# iter = 2
# iter /= 3
# print(iter)

# a = 1 < 4
# print(a)

# print("Введите первое число: ")
# n = int(input())

# x = 0
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
#     print(summa)

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
# print(i)
# 100 80 60 40 20

# for i in range(100, 0, -20):
#     print(i)

# line = ""
# for i in range(3):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'Привет, Виталя! Как твои Дела в програмировании?'
# print(len(text))

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# a = int(input())
# b = int(input())
# c = int(input())

# if a == 2 or b > 2:
#     print("true")


# if 6 <= c and a > 3:
#     print("true")

# if 1 != b and c != 3:
#     print("true")
# if a >= -1 or a <= b:
#     print("true")
# if not (a > 2):
#     print("true")
# if not (c <= 10):
#     print("true")
# else:
#     print("f")

# if a >= 0 and a <= 13:
#     print('детство')
# elif a >= 14 and a <= 24:
#     print('молодость')
# elif a >= 25 and a <= 59:
#     print('зрелость')
# else:
#     print("старость")

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')
# n = int(input())
# if 1000 < n > 100 and (n % 7 == 0 or n % 17 == 0):
#     print("Принадлежит")
# else:
#     print('Не принадлежит')


# def sum_rec(first_number, second_number):
#     if first_number == 0:
#         return second_number
#     return sum_rec(first_number-1, second_number+1)


# # результат записываем во второе число рекурсивно отнимая в первом числе 1 и добавляя ее во второе число.
# # как только первое число станет 0 сработает условие выхода из рекурсии
# a, b = 22, 10
# print(sum_rec(a, b))


# def sumNum(a, b):
#     if a == 0 or b == 0:
#         if a > b:
#             return a
#         return b
#     elif (b == 1):
#         return a + 1
#     return sumNum(a+1, b-1)


# num_1 = int(input('Input first Positive! number: '))
# num_2 = int(input('Input second Positive! number: '))
# print(f'{num_1} + {num_2} = {sumNum(num_1, num_2)}')

# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
# но только на 1 клетку.

a = int(input())
b = int(input())
c = int(input())
max = 0
min = 0
second = 0
if a < b:
    a = max
elif max > c:
    c = max
