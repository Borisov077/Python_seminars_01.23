# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками(то есть разломить шоколадку на два
#                       прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите длину шоколадки: "))
m = int(input('Введите ширину шоколадки: '))
k = int(input("На сколько долек отломить: "))

if (k % m == 0 or k % n == 0) and (k < n*m):
    print(f'Можно отломить за раз такое кол-во долек: {k}')
else:
    print(f'Нельзя отломить за раз такое кол-во долек: {k}')
