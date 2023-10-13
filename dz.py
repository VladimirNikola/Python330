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

import re

s = '+7 499 456-45-78 , +74994564578 , 7 (499) 456 45 78 , 7 (499) 456-45-78'
reg = r'\+?7\s*\(?\d+\)?\s*\d+[- ]?\d+[- ]?\d+'
print(re.findall(reg, s))
