# dz13
# def func(a):
#     numb = ''
#     while a > 0:
#         numb = str(a % 2) + numb
#         a = a // 2
#     print(numb)
#
#
# while True:
#     x = int(input('-> '))
#     if x == 0:
#         break
#     func(x)

# dz14

# s = """Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели. """
# print(s)
# up_e = s.count('Е')
# lower_e = s.count('е')
# count = up_e + lower_e
# print('кол-во слов:', count)

# dz 15

# import re
#
# s = '+7 499 456-45-78 , +74994564578 , 7 (499) 456 45 78 , 7 (499) 456-45-78'
# reg = r'\+?7\s*\(?\d+\)?\s*\d+[- ]?\d+[- ]?\d+'
# print(re.findall(reg, s))

# dz 16
#
# arr = ['Замена строки в текстовом файле;', 'изменить строку в списке;', 'записать список в файл;']
#
# with open('text.txt', 'w') as text:
#     for i in arr:
#         text.write(i + '\n')
#
# full_text = []
#
#
# def read_text():
#     global full_text
#     with open ('text.txt', 'r') as text_:
#         full_text = text_.readlines()
#         for j in full_text:
#             print(j, end='')
#
#
# read_text()
#
# pos1 = int(input('\n' + 'pos1 = ')) - 1
# pos2 = int(input('pos2 = ')) - 1
#
# print()
#
# if 0 <= pos1 <= pos2 <= len(full_text):
#     full_text[pos1], full_text[pos2] = full_text[pos2], full_text[pos1]
# else:
#     print("Индекс введен не верно!")
#
# with open('text.txt', 'w') as text:
#     for i in full_text:
#         text.writelines(i)
#
# read_text()

# dz 17

import os

dir_name = "nested1"

a = os.listdir(dir_name)
print(a)

for obj in a:
    p = os.path.join(dir_name, obj)
    if os.path.isfile(p):
        print(f"{a} - file - {os.path.getsize(p)} bytes")
    elif os.path.isdir(p):
        print(f"{a} - dir")
