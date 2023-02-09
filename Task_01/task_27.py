#  льзователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

# string = input()
# string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# s = set(string.split())
# # print(s)
# print(len(s))

string = "She sells  sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells."

string = string.replace('.', ' ')
string = string.replace(',', ' ')
string = string.replace(';', ' ')
set1 = set(string.upper().split())
print(set1)
print(len(set1))
