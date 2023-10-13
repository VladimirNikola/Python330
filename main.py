# name = "User"
# print("Hello,", name)
# age = 20
# print(age)
# print(type(age))
# age = "hello"
# print(age)
# print(type(age))
import math
import shlex
import time

# a = 4
# print("a =", id(a))
# b = 5
# print("b =", id(b))
# a = b
# print(a)
# print("a =", id(a))

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "hello", 9.21
# print(a, b, c)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# name = "Игорь"
# age = 36
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")

# 16.20дз
# a = 5
# b = 7
# print("a:", a)
# print("b:", b)
# temp = a
# a = b
# b = temp
# print("a:", a)
# print("b:", b)

# print("\tстрока \nсим \"вол\" ов")
# print("C:\\folder\\file.\rtxt")

# print(6 / 2)
# print(6 // 2)

# функции явного преобразования типов
# int
# str


# s1 = "2"
# s2 = 5
# print(int(s1) + s2)
# print(s1 + str(s2))

# print(4523534653467732234234234234234423)
# print(type(4.52353465346772342342342344432423))

# a = 5
# b = 7
# c = 3
# print("Сумма: " + str(a+b))
# print("Произведение: " + str(a*b))
# print("Среднее арифметическое " + str((a+b+c)//3))

# a, b, c = 5, 7, 3
# summ = a + b + c
# pr = a * b * c
# sr = summ / 3
# print('сумма: ', summ, '\nпроизведение: ', pr, '\nсреднее: ', sr)

# number = 6 + 4 * 5 ** 2 + 7
# #              2    1
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5 # num = num + 5
# print(num) # 15
#
# num -= 3 # num = num - 3
# print(num) # 12

# num = 9753 # 43
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# b = num % 10
# print("b:", b)
# num = num // 10
# c = num % 10
# print("c:", c)
# num = num // 10
# d = num % 10
# print("d:", d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 9753
# print("Исходное число:", num)
# res = num % 10 * 1000 # 1000
# num = num // 10
# res += num % 10 * 100 # 200
# num = num // 10
# res += num % 10 * 10 # 30
# num = num // 10
# res += num % 10 # 4
# print(res)

# print(int(3.4789456))
# print(round(3.4789556, 4))


# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a = a + b
# b = a - b
# a = a - b
# print("a:", a)
# print("b:", b)
# b, a = a, b
# print("a:", b)
# print("b:", a)

# a = '5.2'
# b = 10
# print(float(a) + b)

# print(int("5.2"))

# a = 1
# b = 2
# print("a", a, "\nb:", b)

# name = "Виктор"
# age = 21
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут "+ name+ ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end="\n\n")
# print("Привет")

# name = input("Введите  " + "имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print(type(num))
# print(type(power))
# print(res)

# b1 = True  # 1
# b2 = False  # 0
# print(b1 + 5)
# print(b2 + 5)

# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(-0.2))  # True
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(2 + 5 == 7 + 3)

# print(2 < 4 < 9)  # True True
# print(2 * 5 > 7 >= 4+3)  # True True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False


# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True -> True
# print(5 - 3 == 3 and 1 + 3 == 4)  # False and True -> False
# print(5 - 3 == 2 and 1 + 3 == 5)  # True and False -> False
# print(5 - 3 == 3 and 1 + 3 == 5)  # False and False -> False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True and True -> True
# print(5 - 3 == 3 or 1 + 3 == 4)  # False and True -> True
# print(5 - 3 == 2 or 1 + 3 == 5)  # True and False -> True
# print(5 - 3 == 3 or 1 + 3 == 5)  # False and False -> False

# print(not 9 - 5)  # not True => False
# print(not 9 - 9)  # not False => True

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("a == b")

# if a > b:
#     print("a > b")
# if a < b:
#     print("b > a")
# if
#     print("a == b")

# a = int(input('1 сторона треугольника: '))
# b = int(input('2 сторона треугольника: '))
# c = int(input('3 сторона треугольника: '))
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or b == c or a == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')


# day = int(input("Введите день недели цифрой: "))  # 3
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
#
# else:
#     print("Такого дня недели не существует")


# x = int(input("Введите номер месяца: "))
# if x == 12 or x == 1 or x == 2:
#     print("Зима")
# elif x == 3 or x == 4 or x == 5:
#     print("Весна")
# elif x == 6 or x == 7 or x == 8:
#     print("Лето")
# elif x == 9 or x == 10 or x == 11:
#     print("Осень")
# else:
#     print("Неверный номер")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# Дз 16:44

# day = 'вторник'
# time = 16
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 40, 30
# print("a == b" if (a == b) else ("a > b" if (a > b) else "b > a"))

# a = 10
# b = 0
# print("На ноль делить нельзя" if b == 0 else a / b)

# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 1 <= a <= 99:
#     if 11 <= kop <= 14:
#         print(a, "копеек")
#     else:
#         kop = kop % 10
#         if kop == 1:
#             print(a, "копейка")
#         elif 2 <= kop <= 4:
#             print(a, "копейки")
#         else:
#             print(a, "копеек")
# else:
#     print("Некорректное значение")

# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводите строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:  # попытаться
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):  # исключение
#     print("Нельзя вводите строки или нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели ", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")


# n = input("Введите первое число: ")
# m = input("Введите втрое число: ")
#
# try:
#     n = int(n)  # '8'
#     m = int(m)  # 'l'
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)  # 8 + 'l'


# Циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 0
# while i < 20:
#     print("i =", i)
#     i += 1  # i = i - 1

# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# i = 1
# while i <= 10:
#     b = i * 2
#     print(b)
#     i += 1

# i = 2
# while i <= 20:
#     print("i = ", i)
#     i += 2

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите число: "))
# print('*' * a)

# a = int(input("Введите начало диапазона: "))  # 1
# b = int(input("Введите конец диапазона: "))  # 5
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a  # res = res + a => res = 0 + 1
#     a += 1
# print(a)

# n = int(input("Введите число: "))
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите число: ")
#
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1  # i = i + 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# res = 1
# while True:
#     numb = int(input("Введите  число: "))
#     if numb == 0:
#         break
#     res *= numb
# print("Результат:", res)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)

# for i in 'Hello':
#     print(i)

# for color in 'red', 'blue', 'green', 20:
#     print(color)

# print(range(8))
# range(start, stop, step)
#        0,   8,      1

# for i in range(2, 8, 2):  # for(let i=2; i<8; i++)
#     print(i, end=" ")
#
# print()
# j = 2
# while j >= 8:
#     print(j, end=" ")
#     j -= 1

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# a = int(input("Введите целое число: "))
# i = 1
# while i < 100:
#     if a % i == 0:
#         print(i)
#         i += 1

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("\t--")
#         for k in range(2):
#             print("\t\t***")

# a = int(input('Введите Ширину прямоугольника: '))
# b = int(input('Введите Высоту прямоугольника: '))
# for i in range(b):
#     for j in range(a):
#         if i == 0 or i == b - 1 or j == 0 or j == a - 1:
#             print('*', end="")
#         else:
#             print(' ', end="")
#     print()


# a = int(input('Введите Ширину прямоугольника: '))
# b = int(input('Введите Высоту прямоугольника: '))
# for i in range(b):
#     if i == 0 or i == b - 1:
#         print('*' * a)
#     else:
#         print('*' + (' ' * (a - 2)) + '*')

# a = [b * 2 for b in "Banana"]
# print(a)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Список (list)
# nums = [8, 3, 9, 4, 1]
# #       0  1  2  3  4
# #      -5 -4 -3 -2 -1
# # print(nums)
# # print(type(nums))
# # print(nums[0])
# # print(nums[-1])
# # nums[3] = 255
# # print(nums)
# # nums[1] += 100
# print(nums)
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# s1 = list("Hello")
# print(s1)
# print(type(s1))

# n = list(range(10, 2, -2))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]  # [0, 0, 0 , 0 , 0]
# print(a)
#
# d = [v * 3 for v in "list"]
# print(d)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)

# a = [4, 8, 9, 5, 3]
# for i in range(len(a)):  # 0 1 2 3 4
#     print(a[i], end=" ")  # 4 8 9 5 3
# print()
# for i in a:  # 4 8 9 5 3
#     print(i, end=" ")

# res = 0
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in a:
#     if a[i] < 0:
#         res += a[i]
# print(res)

# n = list(range(21, 41))
# print(n)
# for i in n:
#     if i % 2 == 0:
#         print(i, 'Чётные')
#         if i % 3 == 0:
#             print(i, 'Нечётные')

# n = list(range(21, 41))
# print(n)
# count = 0
# nechet = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         nechet += n[i]
# print(count, nechet)

# Дз 16:41

# a = [7, 9, 2, 1, 17]
# a[0], a[1] = a[1], a[0]
# print(a)

# Срезы

# s = [5, 9, 3, 7, 1, 8]
# # список[start:stop:step]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[::-1])
# print(s[5:1:-1])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[0:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:8])
# print(s[-3:1:-1])
# print(s[2:5])

# s = list(range(1, 8))
# print(s)
# s[1:3] = [0, 0, 0, 0]
# # s[1] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[9:10] = [30]
# print(s)

# Методы списков
# s = [1, 20, 0, 0, 0, 4, 5, 6, 7, 30]
# print(s)
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([5, 4, 3])  # добавляет список элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100)  # добавляет элемент (второй параметр) списка в заданный индекс (первый параметр)
# print(s)
#
# s.insert(-1, 200)
# print(s)

# res = 0
# count = 0
# a = [int(input('-->')) for i in range(int(input('Количество элементов: ')))]
# for i in range(len(a)):
#     res += a[i]
#     if a[i] != 0:
#         count += 1
# print(res / count)


# pool = int(input('Введите размер поля: '))
# sim = int(input('Введите количество символов: '))
#
# for i in range(pool):
#     for h in range(sim):
#         for j in range(pool):
#             for k in range(sim):
#                 if (i + j) % 2 == 0:
#                     print('*', end='')
#                 else:
#                     print('  ', end='')
#         print()

# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
#
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])

# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [11, 3, 1, 22, 2, 33, 3, 4, 5]
# # s[3:5] = []
# # del s[:]
# print(s)
# # # n = 11
# # # if n in s:
# #     s.remove(n)  # удалит  элемент из списка по значению
# # last = s.pop(3)  # удаляет элемент по заданному индексу  в круглых скобках, если индекс не передан, то последний элемент из списка
# # print(last)
# s.clear()  # очищает список
# print(s)

# a = [int(input('->')) for i in range(int(input('n = ')))]
# k = int(input('Введите индекс для удаления: '))
# a.pop(k)
# print(a)

# s = [11, 3, 1, 22, 3, 2, 33, 3, 4, 5]
# # # num = s.count(23)  # подсчет количества заданных значений в списке
# # # print(num)
# print(s)
# ind = s.index(2,5)  # возвращает индекс первого элемента, можно передать параметры start и stop
# print(ind)

# s = [11, 3, 1]
# b = s.copy()
# print("s =", s)
# print("b =", b)
# b.append(120)
# s.append(30)
# print("s =", s)
# print("b =", b)

# s = [11, 3, 1, 22, 3, 2, 33, 3, 4, 5]
# # # s.reverse()  # перестраивает элементы в обратном порядке
# # s.sort(reverse=True)  # сортировка по возрастанию, reverse=True - по убыванию
# # print(s)
# n = sorted(s, reverse=True)
# print(s)
# print(n)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s.sort(key=len, reverse=True)
# print(s)


# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(1, 9))
# print(random.randrange(2, 9, 2))

# from random import *
# print(randint(1, 9))
# print(randrange(2, 9, 2))

# import random as r

# print(r.randint(1, 9))
# print(r.randrange(2, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))
#
# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
# print(r.choices(city, k=2))
# r.shuffle(city)
# print(city)

# s = [8, 7, 5, 3, 2, 5, 7, 4, 32, 63, 23, 67]
# print(r.choice(s))
# print(r.choices(s, k=4))

# from random import randint
#
# print([randint(1, 50) for i in range(5)])

# s = [8, 7, 5, 3, 2, 5, 7, 4, 32, 63, 23, 67, 73]
# print(sum(s))
# print(len(s))
# print(min(s))
# print(max(s))


# from random import randint
#
# s = [randint(1, 100) for i in range(10)]
# print(s)
# max_el = max(s)
# print('Max', max_el)
# s.remove(max_el)
# s.insert(0, max_el)
# print(s)

# lst = []
# if not lst: # len(lst) == 0
#     print("Список пустой")
#
# print(bool(lst))

# from random import randint
#
# n1 = int(input("Размер первого списка: "))
# n2 = int(input("Размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("Третий список:", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#

# print("Элементы обоих списков без повторений:", c)

#  Продолжение с 11 пары

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# print(m)
# print(m[1][2])
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for i in m:
#     for j in i:
#         print(j * j, end='\t')
#     print()

# w, h = 5, 3
# m = [[y*x for x in range(w)] for y in range(h)]
# # m = []
# # for y in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     m.append(new_row)
# print(m)
#
# for i in m:
#     for j in i:
#         print(j * j, end='\t')
#     print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# from random import randint
# w, h = 3, 4
# m = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# res = 0
# for i in m:
#     for j in i:
#         if j < 0:
#             res += 1
#         print(j, end='\t')
#     print()
# print("Количество отрицательных элементов:", res)


# import math
#
# num1 = math.sqrt(4)
# # num2 = round(5.925654, 2)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.9)
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# sec = time.time()
# print(sec)
#
# local = time.ctime(465467232)
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))
#
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "sec")

# text = input("Название напоминания: ")
# locale_time = float(input("Через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# 15.35 пропустил


# Функции

# def hello(name):  # аргументы
#     print("Hello", name)
#
#
# hello("Irina")  # параметры
# hello("Ivan")

# def get_sum(a, b):
#     print(a + b)
#
#
# a1 = 2
# b1 = 5
# get_sum(a1, b1)
# n = 10
# m = 20
# get_sum(n, m)


# def x(sym1, sym2, numb):
#     for i in range(numb):
#         if i % 2 == 0:
#             print(sym1, end='')
#         else:
#             print(sym2, end='')
#     print()
#
#
# x('+', '-', 9)
# x('0', 'X', 7)

# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# a1 = 2
# b1 = 5
# res = get_sum(a1, b1)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))

# def coil(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# first = int(input("a = "))
# second = int(input("b = "))
# res = coil(first, second)
# print("Результат:", res)


# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', "л", "о", "н"]))

# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# if func(10, 5):
#     print("Первое число больше")
# else:
#     print("Второе число больше")


# Проверка пароля
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "А" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это не надежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# num = 2
# print(get_sum(1, 5, d=num))


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         if i == 0 or i == b - 1 or j == 0 or j == a - 1:
#             print('*', end="")
#         else:
#             print(' ', end="")
#     print()


# Кортeж(tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5, 6
# print(a)
# print(type(a))

# from random import randint


# s = tuple(randint(0, 100) for i in range(5))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# t4 = t1 * 3
# print(t4)
# print(t3.count('l'))
# print(t3.index('l', 4))

# for i in t3:
#     print(i, end=' ')

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1)  # 4
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
# def rnd_tpl(a, b):
#     s = tuple(randint(a, b + 1) for i in range(10))
#     return s
#
#
# n = rnd_tpl(0, 5)
# m = rnd_tpl(-5, 0)
# print(n)
# print(m)
# x = n + m
# print(x)
# print(x.count(0))

# t = (10, 11, [1, 2, 3], [4, 3, 6], ["Hello", 'world'])
#
# print(t[4][0])
# t[4][0] = "new"
# t[4].append("h1")
# print(t)


# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # first_name, year, married = user
# print(first_name, year, married)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lt = list(tpl)
# print(lt)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамберг", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, ", Население: ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население: ", city_population, sep="")


# Множества (set) - Хранит уникальные данные

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))

# a = set("Hello")
# print(a)
# print(type(a))

# s = ("banana", "apple", "orange", "banana", "apple")
# print(s)
# s1 = set(s)
# print(s1)
# s2 = list(s1)
# print(s2)

# s = {x * x for x in range(10)}
# print(len(s))


# def to_set(lst):
#     x = set(lst)
#     return x, len(x)
#
#
# print(to_set("я боычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {"red", "green", "blue"}
# # print("green" in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', "bc_1", 'bc_2']
# print(r)
# # a = {i for i in r if 'a' in i}
# # a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r}
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == "a":
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# r1 = {'ab_1', 'ac_2'}
# r2 = {'bc_1', 'bc_2'}
# print(r1 + r2)

# user = {"Tom", "Bob", "Alice"}
# print(user)
# # user.remove("Tom1")
# # user.discard("Tom")
# # user.pop()
# # user.clear()
# user.add("Ann")
# print(user)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# print(c)
# a | b = b
# print(a)
# c = a & b
# print(c)
# a &= b
# print(a)
# c = a ^ b
# print(c)
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}

# s = s1.union(s2, s3, s4, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# str1 = set("Hello")
# str2 = set("How are you")
# str3 = set(str1) & set(str2)
# print(str3)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)

# drawing = {'Марина', "Женя", "Света"}
# music = {"Кости", "Женя", "Илья"}
#
# only_one = drawing ^ music
# print(only_one)
# both = drawing & music
# print(both)
# drawing = drawing - both
# print(drawing)

# Дз
# from random import randint
#
# n1 = int(input("Размер первого списка: "))
# n2 = int(input("Размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("Третий список:", c)

# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#
# print("Элементы обоих списков без повторений:", c)

# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print("Элементы общие для двух списков:", c)

# c = [min(a), min(b), max(a), max(b)]
#
# print("Минимальное и максимальное значение каждого из списков:", c)
#  -


# Словарь (dict)
# d = {}

# s = ['a', 'b', 'c']
# d = {}
# print(s)
# print(d)
# print(s[0])
# print(d['one'])

# users = ([
#     ('one', 'a'),
#     ('two', 'b'),
#     ('tree', 'c')
# ])
# print(users)
# d = dict(users)
# print(d)


# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[0])
# d[0] = 15 * 2
# print(d)

# d = {'one': 'a', 'two': 'b', 'tree': 'c'}
# # for i in d:
# #     print(i, '-->', d[i])
#
# del d['one1']
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for i in d:
#     res *= d[i]
# print(d)
# print(res)

# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# disl = int(input("Какой элемент исключить: "))
# del d[disl]
# print(d)


# x = {1: 3, 2: 7, 3: 5, 4: -1}
# print(len(x))

# -
# x = {
#     1: ['Core-i3-4330', 9, '4500руб'],
#     2: ['Core-i5-4670K', 3, '8500руб'],
#     3: ['AMD FX-6300', 6, '3700руб'],
#     4: ['Pentium G3220', 8, '2100руб'],
#     5: ['Core-i5-345', 5, '6400руб']
# }
#
#
# def port():
#     for i in x:
#         print(f'{i}) {x[i][0]} - {x[i][1]} шт. по {x[i][2]}руб')
#
#
# port()
#
# while True:
#     j = int(input('№: '))
#     if j == 0 or j > len(x):
#         break
#     else:
#         x[j][1] += int(input('Количество: '))
#
# port()
# -

# Методы словарей
# d = {'one': 'a', 'two': 'b', 'tree': 'c'}
# print(d.keys())  #  'one', 'two', 'tree'
# print(d.values())  #  'a', 'b', 'c'
# print(d.items())  #  ('one', 'a'), ('two', 'b'), ('tree', 'c')
# # for i, j in d.values():
# #     print(i, '->', j)
# s = list(d.items())
# print(s)

# d = {'one': 'a', 'two': 'b', 'tree': 'c'}
#
# # value = d['one']
# # value = d.get('one1', 'Такого ключа нет')
# # print(value)
# # d2 = d
# # print("D =", d)
# # print("D2 =", d2)
# #
# # d['four'] = 'd'
# # print("D =", d)
# # print("D2 =", d2)
# # item = d.pop('two2', "Такого ключа не существует")
# # print(item)
# # print(d)
# # item = d.popitem()
#
# # d.clear() # Очищает словарь
# # print(d)
# # a = {'four': 'd', 'two': 'last'}
# d.update([('four', 'd'), ('two', 'last')])  # Добавляет
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
#
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# x = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'}
#
# # d = dict()
# # d['name'] = x.pop('name')
# # d['salary'] = x.pop('salary')
# # print(x)
# # print(d)
#
# x['location'] = x.pop('city')  # Меняет ключ
# print(x)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d2 = {k: v for k, v in d.items() if v <= 2}
# print(d2)

# -
# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")
# -

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d = {"one": []}
#         s = i  # "one"
#     else:
#         d[s].append(i)  # d = {"one": [1,2,3]}
# print(d)


# All__winners = ['Наталья', 'Максим', 'Евгения', 'Александр', 'Матвей', 'Михаил']
# print('Все призеры: ', All__winners)
# math = {'Наталья', 'Максим', 'Евгения', 'Матвей', 'Михаил'}
# physics = {'Максим', 'Матвей', 'Александр'}
# b = math & physics
# print('Призеры обеих олимпиад: ', b)
# c = b
# print('Обновленный список призеров по математике: ', c)

# sale = {
#     'Join': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'B': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
#
# for x in sale:
#     print(x)
#     for y in sale[x]:
#         print('\t', y, ": ", sale[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sale[person][region])
# new_data = int(input("Новое значение: "))
# sale[person][region] = new_data
# print(sale[person])

# a = {1, 2, 3, 4, 5}
# # b= ['one', 'two', 'three']
# # c = [4.0, 5.5, 6.2]
# d = list(zip(a))  # b, c
# print(d)

# one = {'name': 'Igor', 'surname': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'surname': 'Smith', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# pairs = [(4, 'two'), (2, 'one'), (6, 'three')]
# a, b = zip(*pairs)
# print(a)
# print(b)
#
# data = list(zip(b, a))
# print(data)
#
# data.sort()
# print(data)
#
# # data.reverse()
# # print(data)
#
# data = dict(data)
# print(data)
#
# f = {v: k for k, v in data.items()}
# print(f)
# f = list(f.items())
# print(f)

# one = {'apple': 0.45, 'orange': 0.35, 'pepper': 0.35}
# two = {'pepper': 0.25, 'union': 0.55}
# print({**one, **two})  # {'apple': 0.45, 'orange': 0.35, 'pepper': 0.25, 'union': 0.55}
#
# for k, v in {**one, **two}.items():
#     print(k, '->', v)

# colors = ['red', 'blue', 'green']
# for i in range(len(colors)):
#     print(i + 1, ") ", colors[i], sep="")
# print()
# j = 1
# for color in colors:
#     print(j, ") ", color, sep="")
#     j += 1
# print()
# for v, color in enumerate(colors, start=1):
#     print(v, ") ", color, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     print(*args)
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(5, 9, 4))


# def to_dict(a, b, c, d):
#     i = (a, b, c, d)
#     return dict(zip(i, i))

# def to_dict(*args):
#     return {i: i for i in args}


# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def ch(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 5, 9, 7))

# def print_scores(stud, *scores):
#     print("students name", stud)
#     for score in scores:
#         print(score)
#
#
# print_scores("Jonathan", 100, 95, 88, 92, 99, 65)
# print_scores("Rick", 98, 20, 30, 56)

# def func(**kwargs):
#     print(kwargs)
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))

# def info(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#
#
# info(surname="Sharma", name="Irina", age=22, phone=1234567890)
# info(surname="Wood", name="Igor", email="igor@mail.ru", country="Russia", age=25, phone=6789012345)

# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)

# name = "Tom"
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
# print(name)
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
#
# i = 6
# func()  # 5

# def add(a):
#     x = 2
#
#     def add_some():
#
#         print("x =", x)
#         return a + x
#
#     print("XXX", x)
#     return add_some()
#
#
# print(add(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t, end=", ")


# sum = 5
# print(sum)
#
# lst = [5, 9, 7, 1, 6, 4, 8]
# print(sum(lst))

# print = 5
# s = 2
# print(s)

# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print("a:", a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# c = x + t  # 25 + 30 = 55
# print(c)

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))
#
# b = outer(6)
# print(10)
#
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#     print("a = 1", id(a))
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         # print("a = 2", id(a))
#         b = b + "_!!!"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     c = 0
#
#     def inner():
#         nonlocal c
#         c += 1
#         print(city, c)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# b_A = outer(80, 100)
# b_B = outer(70, 80)
# b_C = outer(50, 70)
# b_D = outer(0, 50)
# print("A: ", b_A(students))
# print("B: ", b_B(students))
# print("C: ", b_C(students))
# print("D: ", b_D(students))


# def outer(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj = outer(5, 2)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())


#  Lambda - выражения (анонимные функции)

# func = lambda x, y: x + y
# print(func(1, 2))
#
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20, ))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
# print((lambda *args: sum(args))(10, 20, 30))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t('abc__'))

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# f = outer(10)
# print(f(5))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# f1 = outer1(10)
# print(f1(5))
#
# outer2 = lambda n: lambda x: n + x
# f2 = outer2(10)
# print(f2(5))
#
# print((lambda n: lambda x: n + x)(10)(5))

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {'b': 25, 'a': 15, 'c': 24}
# # lst = list(d.items())
# # print(lst)
# # lst.sort(key=lambda i: i[1])
# # print(lst)
# # print(dict(lst))
# new_d = sorted(d.items(), key=lambda i: i[1])
# print(new_d)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res1 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res1)
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# res2 = min(players, key=lambda item: item['name'])
# print(res2)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[0](12, 2))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
# }
#
# d[4]()

# area = {
#     'circle': lambda r: 3.14 * r ** 2,
#     'triangle': lambda a, b: a * b,
#     'trapezoid': (lambda a, b, h: (a + b) * h / 2)
#
# }
#
# print("Площадь окружности", area['circle'](2))
# print("Площадь прямоугольника", area['triangle'](10, 13))
# print("Площадь трапеции", area['trapezoid'](7, 5, 3))

# print((lambda a, b: a if a > b else b)(15, 23))
# print((lambda a, b, c: a if (a <= b) and (a <= c) else b if (b <= a) and (b <= c) else c)(4, 3, 2))

# map(func, *iter), filter(func, *iter)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))

# t = (2.28, 6.44, 100.4)
#
# print(tuple(map((lambda x: int(x)), t)))
# print(tuple(map(int, t)))

# Дз
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(s)
# print(outer(5, 8, 2))
# print(s)
# print(outer(1, 6, 8))
# print(s)

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))

# filter(func, *iter)

# t = ('abcd', 'abc', 'casdf', 'def', 'ghj')
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# print('abcd' * 2)


# from random import randint
#
# b = [randint(1, 40) for i in range(10)]
# print(b)
# res = list(filter(lambda s: 10 <= s <= 20, b))
# print(res)

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decor(fn):
#     def wrap(args1, args2):
#         print(args1, args2)
#         fn(args1, args2)
#
#     return wrap
#
#
# @args_decor
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лазарева")

# def args_decor(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decor
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "Изучают", study, "\n")
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study='JavaScript')
# print_full_name("Владимир", " Екатерина", "Виктор")

# @typed(int, int, int)
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:  # type(x) != int
#                     raise TypeError("Некорректный тип данных", f_args[i])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# def typed_fn2(x, y, x):
#     return x + y + z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# # print(typed_fn(3.6, 4.5, 7.8))
# print(typed_fn2("Hello, ", "World", "!"))
# print(typed_fn2(3, 4, 5))

# def sr_a(fn):
#     def wrap(*f_args):
#         x = fn(*f_args)
#         print('Среднее арифметическое чисел', end=' ')
#         print(*f_args, sep=', ', end=' ')
#         print('=', x / len(f_args))
#
#     return wrap
#
#
# @sr_a
# def summa(*args):
#     res = 0
#     for i in args:
#         res += i
#     print('Сумма чисел', end=' ')
#     print(*args, sep=', ', end=' ')
#     print('=', res)
#     return res
#
#
# summa(2, 3, 3, 4)
# def changeCharTostr(s, c_old, c_new):
#     s2 = ""
#
#     for i in s:
#         if i == c_old:
#             s2 += c_new
#             continue
#         s2 += i
#
#     return s2
#
#
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython очень интересный язык программирования."
# str2 = changeCharTostr(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)
#
#
# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")
#
# round(f"{round(3.15673123), 2}")
# print(f"{3.434367:.3f}")


# x = 10
# y = 6
# # print("x =", x)
# # print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# nem = 74
# print(f"{{{{{nem}}}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home" + "\\" + dir_name + "\\" + file_name)

# def square(n):
#     """Принимает число n, возвращает квадрат число n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительно число, радиус основания цилиндра
#     :param h: положительно число, высота цилиндра
#     :return: положительно число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

#
# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# a, b = 97, 122
# if a > b:
#     arr = [chr(i) for i in range(b, a + 1)]
#     print(' '.join(arr))
# else:
#     arr = [chr(i) for i in range(a, b + 1)]
#     print(' '.join(arr))
# if a < b:
#     a, b = b, a
# arr = [chr(i) for i in range(b, a + 1)]
# print(' '.join(arr))

# print(("apple" == "Apple"))
# print(("apple" > "Apple")) # 97 > 65


# Случайный пароль

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += rand_char
#     return res
#
#
# print("Случайный пароль:", random_password())

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # Преобр. в ниж регист
# print(s.upper())  # Преобр. в верх регист
# print(s.swapcase())  #
# print(s.title())

# s = "hello, WORLD! I am learning Python."

# print(s.count("h", 1, -4)) # count делает подсчет строковых символов
# print(s.find("l", 4, 19))  # find находит совпадение и выводит число индекса, если он не нашел совпадение то покажет индекс -1

# print(s.find("l"))  # Производит поиск слева на право(индекск)
# print(s.rfind("l"))  # Производит поиск с право на лево(индекс)
# print(s.index("l"))  # Производит поиск слева на право(индекск)
# print(s.rindex("l")) # Производит поиск с право на лево(индекс)

# text = input("Введите два слова: ")  # 'один два'
# a = text[:text.find(' ')]  # text[:4] => один
# b = text[text.find(' ') + 1:]  # text[5:] => два
# new_text = b + ' ' + a  # два один
# print(new_text)

# s = "hello, WORLD! I am learning Python."
#
# print(s.index("I am"))  # 14 индекс
# print(s.startswith(("I am", "hello")))  # True
# print(s.endswith("Python."))  # True если в конце строки

# a = "456"
# print(int(a))

# print('abc123'.isalnum())  # Будет возвращать True если строка не пуста. Поддерживает цифры и буквы
# print('ABCabc'.isalpha())  # Будет возвращать True если буквы в любом регистре
# print('123'.isdigit())  # Будет возвращать True если цифры

# print('abc12%^&'.islower())  # Будет возвращать True если буквы в нижнем регистре и есть спец символы
# print('ABC45&*'.isupper())  # Будет возвращать True если буквы в верхнем регистре и есть спец символы

# print('py'.center(10))  #     py
# print('py'.center(10, "-"))  # ----py----


# print("                py".lstrip())  # убирает пробельные символы с лево
# print("py                ".rstrip())  # убирает пробельные символы с право
# print("       py         ".strip())  # убирает пробельные символы с право и слево
# print('https://www.python.org'.lstrip("/:pths"))  # Удаляет перечень запроса слева
# print('py.$$$;'.rstrip(';$.'))  # Удаляет перечень запроса с право

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python", 2))  #Поиск и заменя количества слов

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))  # Объединяет между букв
#
# print("..".join(['1', '2']))  # Объединяет между цифр
#
#
# print(":".join("Hello"))  # Объединяет между букв

# print('Строка разделенная пробелами'.split())  # Разделяет строку пробелами
# print('www.python.org'.split('.', 1))  # Количество разбиения по точке с лево
# print('www.python.org'.rsplit('.', 1))  # Количество разбиения по точке с право
# print('www...python...org '.split("."))

# a = input("Введите ФИО: ").split()
# print(f"{a[0]} {a[1][0]}. {a[2][0]}.")

# a = input("-> ").split()  # Количество разбиения по точке с лево
# a = list(map(int, a))  # Преобразует тип данных из строковой в числовое
# print(a)
# print(type(a[0]))


# Регулярные выражения

# import re  # Модуль с работой регулярных выражений - в console прописываем dir(re) для просмотра методов функционала

# s = "Я ищу совпадения в 2023 году. И я их найду в счёта."
# reg = ' '
#
# # print(re.findall(reg, s))  # список, содержащий все совпадения
# # print(re.search(reg, s))  # месторасположение первого совпадения
# # print(re.search(reg, s).span())  # Получает доступ к кортежу
# # print(re.search(reg, s).start())  # Начало свопадения
# # print(re.search(reg, s).end())  # Конец совпадения
# # print(re.search(reg, s).group())  # Находит слово по запросу
# #
# # print(re.match(reg, s))  # поиск по заданному шаблону в начале строки
# # print(re.split(reg, s, 3))  # Возвращает список строк, разбитых по шаблону разделителю
#
# print(re.sub(reg, "!", s, 3))  # Поиск и замена

# s = "Я ищу совпадения в 2023 году. И я их найду в счёта. 9178"
# # reg = '[12][0-9][0-9][0-9]'
# # reg = r'[A-Za-z0+.\[\]-]'
# reg = r'[^0-9]'
# print(re.findall(reg, s))  # Возвращает все совпадения

# print(ord("А"))
# print(ord("Я"))
# print(ord("Ё"))
# print(ord("а"))
# print(ord("я"))
# print(ord("ё"))

# t = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:59."
# p = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(p, t))

# s = "Я ищу совпадения в 2023 году. И я их найду в счёта.  [H^el_lo] 9178"
# # reg = r'\w+'
# reg = r'20*'
# \d - поиск цифр
# \s - поиск пробельного символа
# \w - поиск букв цифр и символ подчеркивания _
# \D - поиск все что угодно кроме цифр
# \S - поиск все что угодно кроме пробела
# \W - поиск все кроме букв цифр и символов подчеркивания_
# r'9178\Z' - ищет символы в конце строки
# print(re.findall(reg, s))

# text = 'Ежевику для ежат ' \
#        'Принеси два ежа. ' \
#        'Ежевику еле-еле ' \
#        'Ежата возле ели съели'
#
# print(text)
# text_arr = text.split(' ')
# count = 0
# for i in text_arr:
#     if i[0] == 'е' or i[0] == 'Е':
#         count += 1
#
# print(count)

# s = """Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели. """
# print(s)
# up_e = s.count('Е')
# lower_e = s.count(' e')
# count = up_e + lower_e
# print('кол-во слов:', count)

# d = 'Цифры: 7, +17, -42, 0013, 0.345456654'
# print(re.findall(r'[+-]?\d+\.?\d*', d))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub("#.+", "", s))


# s = "12 сентября 2023 года"
# reg = r'\d{2,4}'
# print(re.findall(reg, s))


# s = '+7 499 456-45-78 , +74994564578 , 7 (499) 456 45 78 , 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в счё-та."
# # reg = r'^\w+\s\w+'
# reg = r'^\w+\.$'
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall('^[A-Za-z_-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('!!!Python_master'))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
# print(re.findall(r'\w+', '12 + й', flags=re.A))

# text = 'hello world'
# print(re.findall(r'\w\+', text, re.DEBUG))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё-та."
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """

# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one.\w+', text, re.S))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))
# print(re.findall(r'one$', text, re.M))

# print(re.findall("""
# [a-z. -]+   # part 1
# @           # @
# [a-z.-]+    # part 2
# """, 'test@mail.ru', re.VERBOSE))


# text = """Python
# python
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*>", text))  # [<body>, </body>]

# s = "<p>Изображение <img src='bg.jpg'> - Фон страницы</p>"
# reg = r'<img\s+[^>]*src\s*\s*[^>]+>'
# print(re.findall(reg, s))  # [<img src='bg.jpg'> ]


# n = int(input("-> "))
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
#
# print(b)

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

# f = open("test.txt")
# print(f)
# print(*f)
# print(f.mode)
# print(f.)
# print(f.mode)
# f.close()
# print(f.closed)

# f = open("D:\\Учеба\\Python\\test.txt")
# # f = open("D:\Python330\test.txt")
# print(f.read(3))
# print(f.read())
# f.close()

# f = open("test.txt", "r")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# f.close()


# f = open("test.txt", "r")
# print(f.readlines(3))
# f.close()

# count = 0
# f = open("test.txt", "r")
#
# for line in f:
#     count += 1
# f.close()
# print(count)
#
# f = open("xyz.txt", "w")
# f.write("Hello \nWorld")
# f.close()
#
# f = open("xyz.txt", "a")
# f.write("\nNew text.")
# f.close()

# f = open("xyz.txt", "a")
# line = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(line)
# f.close()

# f = open("xyz.txt", "w")
# lst = [i for i in range(1, 20)]
# print(lst)  # '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]'
# # t = "\t".join(map(str, lst))
# for index in lst:
#     f.write(index + '\t')
# f.close()
#

# f = open("text2.txt", 'w')
# f.write("Замена строки с текстовом файле; \nизменить строку в списке;\nзаписать список в файле;\n")
# f.close()
#
# f = open("text2.txt", 'r')
# in_put = int(input("Чисел: "))
# read_file = f.readlines()
# if 0 <= in_put < len(read_file):
#     del read_file[in_put]
# else:
#     print("Иднекс введен некорректно!")
# print(read_file)
# f.close()


# f = open("test.txt", "r")
# print(f.read(3))
# print(f.tell())  # Позиция условного курсора
# print(f.seek(1))
# print(f.read())
# f.close()

# f = open("test.txt", "r+")
# print(f.write('I am learning Python'))  # 20
# print(f.seek(3))  # 3
# print(f.write("-new string-"))  # 12
# print(f.tell())  # 15
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line[:3])


# file = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     return " ".join((map(str, lt))
#
#
# with open(file, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")
#
# with open(file, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# nums_list = list(map(float, nums.split()))
# print(nums_list)
# print(sum(nums_list)
# print(min(nums_list)

# def longest_words(file):
#     with open(file, "r", encoding="utf-8") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words("test.txt"))

# read_file = "one.txt"
# write_file = "two.txt"
# third = "three.txt"
# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open(read_file, 'w') as f:
#     f.write(text)

# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# read_file = "one.txt"
# write_file = "two.txt"
# third = "three.txt"
#
# with open(read_file, 'r') as f1, open(write_file, 'r') as f2, open(third, 'w') as f3:
#     file_1 = f1.readlines()
#     file_2 = f2.readlines()
#     f4 = file_1 + file_2
#     f3.writelines(f4)

# arr = ['Замена строки в текстовом файле;', 'изменить строку в списке;', 'записать список в файл;']
# with open('text.txt', 'w') as text:
#     for i in arr:
#         text.writelines(i + '\n')
# full_text = []def read_text():    global full_text    with open('text.txt', 'r') as text_:       full_text = text_.readlines()
# for j in full_text:            print(j, end='')
# read_text()
# pos1 = int(input('\n' + 'pos1 = ')) - 1
# pos2 = int(input('pos2 = ')) - 1
# print()
# full_text[pos1], full_text[pos2] = full_text[pos2], full_text[pos1]
#
# with open('text.txt', 'w') as text:
#     for i in full_text:
#         text.writelines(i)
#         read_text()

# Модули OS и OS.PATH

# import os
# import os.path

# print(os.getcwd())  # возвращает путь к текущей директории
# print(os.listdir())  # список файлов и директорий(папки)
# print(os.listdir(".."))
# print(os.listdir(r"D:\Учеба\JavaScript"))

# os.mkdir("folder_2")  # создание директории(папку)
# os.makedirs("nested1/nested2/nested3")  # создает не только конечную директорию, но и промежуточные

# os.rmdir("folder_2")  # Удаляет папку если пустой каталог
# os.rename('xyz.txt', 'x.txt')  # Переименование файлов и каталогов

# os.rename("x.txt", 'nested1/x.txt')  # Перемещение файла в папку

# os.renames("two.txt", 'text/two.txt')  # перемещение файла в папку(создавая промежуточные директории)

# os.remove('three.txt')  # Удаление файла

# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root", root)
#     print("Subdirs", dirs)
#     print("Files:", files)
#     print()


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root)):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print('-' * 50)
#
#
#
# remove_empty_dirs("nested1")

# import os


# /Users/daniilfil/PycharmProjects/pythonProject/nes

# print(os.path.split(r"D:\Учеба\Python\nested1\nested2\test.txt")[1])  # Windows
# # print(os.path.split("/Users/daniilfil/PycharmProjects/pythonProject/nes"))  # Apple
#
# print(os.path.dirname(r"D:\Учеба\Python\nested1\nested2\test.txt"))
# print(os.path.basename(r"D:\Учеба\Python\nested1\nested2\test.txt"))
#
# print(os.path.join("files", r"D:\Учеба", "folder", "dir", "two.txt"))
# print(os.path.join("nes", "/Users", "daniilfil ""PycharmProjects", "PycharmProjects", "nes"))

# import os

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()

# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# import os
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'Сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fls in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(fls)
#     print("-" * 50)
#
#
#
# print_tree("Work", False)
# print_tree("Work", True)

# import os
# import time

# print(os.path.exists(r'D:\Учеба\Python\Work'))  # Возвращается True, если path указывает на существующий путь в файловой системе
# print(os.path.isfile(r'D:\Учеба\Python\Work\w.txt'))  # Проверка на наличие по заданному пути файла
# print(os.path.isdir(r'D:\Учеба\Python\Work\w.txt'))  # Проверка на наличие по заданному пути файла

# path = 'main.py'
# print(os.path.getsize(path))  # 71464 - в байтах
# print(os.path.getsize(path) / 1024)
# print(os.path.getatime(path))  # последний доступ к файлу
# print(os.path.getctime(path))  # время создания файла (windows) или время последнего изменения (Unix)
# print(os.path.getmtime(path))  # время последнего изменения в секундах
#
# c = os.path.getctime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# 'my-p@ssw0rd'


# Дз валидация номера телефона

import re

s = '+7 499 456-45-78 , +74994564578 , 7 (499) 456 45 78 , 7 (499) 456-45-78'
reg = r'\+?7\s*\(?\d+\)?\s*\d+[- ]?\d+[- ]?\d+'
print(re.findall(reg, s))


# Разобрать дома
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# # print(len(names))
# # print(names[0])
# # print(isinstance(names[1], list))
# # print(isinstance(names[1][0], list))
# # print(names[1][1][0])
# # print(isinstance(names[1][1][0], list))
#
#
# def count_items(item_list):  # ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert']
#     count = 0  # 1  # 1  #
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " " or text[0] == "!":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hel!!lo\tWor!!!ld "))

# Объектно Ориентированное Программирование
# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
# print(p1.x)
# print(p1.y)
# p1.x = 5
# p1.y = 7
# p1.z = 3
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# # print(type(p1))
# p2 = Point()
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)
# print(id(Point.x))  # 1850432451248
# print(id(p1.x))  # 1850430192464
# print(id(p2.x))  # 1850430192400

# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# # p1.set_coord(5, 10)
# Point.set_coord(p1, 5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# # p2.x = 3
# # p2.y = 7
# p2.set_coord(3, 7)
# print(p2.__dict__)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = 'street, house'
# 
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
# 
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.address = address
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
# 
#     def set_phone(self, phone):  # Устанавливает значент
#         self.phone = phone
# 
#     def get_phone(self):  # получает значение
#         return self.phone
# 
#     def set_name(self, name):
#         self.name = name
# 
#     def get_name(self):
#         return self.name
# 
# 
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_phone("55-99-33")
# print(h1.get_phone())
# h1.set_name("Валерия")
# print(h1.get_name())

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print("Инициализатор класса Person")
#
#     def __del__(self):
#         print("Удаление экземпляра класса")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
#
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


