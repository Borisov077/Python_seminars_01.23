# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

digit = int(input("Введите трехзначное число: "))

firstdigit = digit/100
seconddigits = digit // 10 % 10
thirdDidgits = digit % 10
sum = firstdigit + seconddigits + thirdDidgits
print(sum)