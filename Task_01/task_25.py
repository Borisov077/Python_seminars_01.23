# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
#  Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

text = 'a a a b c a a d c d d'
text = text.split()
result = ''
d = {}
for i in range(len(text)):
    if text[i] not in d:
        d[text[i]] = 1
        result += f'{text[i]} '
    else:
        result += f'{text[i]}_{d[text[i]]} '
        d[text[i]] += 1


print(result)
print(d)

#    3 = 'a a a b c a a d c d d'
# s = s.split()
# print(s)

# my_dict = dict()
# for i in set(s):
#     my_dict[i] = -1

# for i in s:
#     my_dict[i]+=1
#     if my_dict[i] == 0:
#         print(i, end=' ')
#     else: print(i, end=f'_{my_dict[i]} ')
