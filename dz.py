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
# import math
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
# import os
#
# dir_name = "nested1"
#
# a = os.listdir(dir_name)
# print(a)
#
# for obj in a:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f"{a} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{a} - dir")

# Dz 18
# class Car:
#     model = ""
#     year = "0"
#     manufacturer = ""
#     engine_volume = "0.0"
#     color = ""
#     price = "0.0"
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(
#             f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\nМощность двигателя: {self.engine_volume}\nЦвет машины: {self.color}\nЦена: {self.price}")
#         print("=" * 40)
#
#     def input_info(self, model, year, manufacturer, engine_volume, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_volume = engine_volume
#         self.color = color
#         self.price = price
#
#     def set_model(self, model):  # Устанавливает значение
#         self.model = model
#
#     def get_model(self):  # получает значение
#         return self.model
#
#     def set_year(self, year):
#         self.year = year
#
#     def get_year(self):
#         return self.year
#
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#     def set_engine_volume(self, engine_volume):
#         self.engine_volume = engine_volume
#
#     def get_engine_volume(self):
#         return self.engine_volume
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# car = Car()
# car.input_info("X7 M50i", 2021, "BMW", "530 л.с.", "white", 10790000)
# car.print_info()
# car.set_model("Q8")
# print(car.get_model())
# car.set_year("2021")
# print(car.get_year())
# car.set_manufacturer("Audi")
# print(car.get_manufacturer())
# car.set_engine_volume("440 л.с.")
# print(car.get_engine_volume())
# car.set_color("blue")
# print(car.get_color())
# car.set_price("7800000")
# print(car.get_price())

# dz 19
# import math
#
#
# class Rectangle:
#     def __init__(self, breadth, length):
#         self.__breadth = breadth
#         self.__length = length
#
#     @property
#     def breadth(self):
#         return self.__breadth
#
#     @breadth.setter
#     def breadth(self, val):
#         if Rectangle.check_value(val):
#             self.__breadth = val
#         else:
#             print("Неверный тип данных")
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, val):
#         if Rectangle.check_value(val):
#             self.__length = val
#         else:
#             print("Неверный тип данных")
#
#
#     @staticmethod
#     def check_value(s):
#         if isinstance(s, (int, float)):
#             return True
#         return False
#
#     def square(self):
#         return self.__breadth * self.__length
#
#     def perimeter(self):
#         return (self.__breadth + self.__length) * 2
#
#     def hypotenuse(self):
#         return round(math.sqrt(self.__breadth ** 2 + self.__length ** 2), 2)
#
#     def print_rectangle(self):
#         print(("*" * self.__breadth + "\n") * self.length)
#
#
# a = 15
# b = 8
# obj = Rectangle(a, b)
# # print("Длина прямоугольника:", obj.length)
# # print("Ширина прямоугольника:", obj.breadth)
# obj.length = 3
# obj.breadth = 9
# print("Длина прямоугольника:", obj.length)
# print("Ширина прямоугольника:", obj.breadth)
# print("Площадь прямоугольника:", obj.square())
# print("Периметр прямоугольника:", obj.perimeter())
# print("Гипотенуза прямоугольника:", obj.hypotenuse())
# obj.print_rectangle()

# dz 20

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет №{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет №{self.__num} принадлежащий {self.__surname} был закрыт.")
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_surname(self, val):
#         self.__surname = val
#
#     def get_num(self):
#         return self.__num
#
#     def set_num(self, val2):
#         self.__num = val2
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_percent(self, val3):
#         self.__percent = val3
#
#     def get_value(self):
#         return self.__value
#
#     def set_value(self, val4):
#         self.__value = val4
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f"№{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print('-' * 20)
#
#
# acc = Account("Долгих", '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет №{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет №{self.__num} принадлежащий {self.__surname} был закрыт.")
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, val1):
#         self.__num = val1
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, val2):
#         self.__surname = val2
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, val3):
#         self.__percent = val3
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, val4):
#         self.__value = val4
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f"№{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print('-' * 20)
#
#
# acc = Account("Долгих", '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()

# dz 21

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def get_color(self):
#         return self.__color
#
#     def set_color(self, color):
#         self.__color = color
#
#
# class Rectangle(Figure):
#
#     def __init__(self, w, h, color):
#         self.verify(w)
#         self.verify(h)
#         self.__w = w
#         self.__h = h
#         super().__init__(color)
#
#     def square(self):
#         return self.__w * self.__h
#
#     @staticmethod
#     def verify(val):
#         if val < 0:
#             raise ValueError('Переменная не должна быть отрицательной')
#
#     def get_info(self):
#         print(f'Высота: {self.__h}'
#               f'\nШирина: {self.__w}'
#               f'\nЦвет: {self.get_color()}'
#               f'\nПлощадь: {self.square()}')
#
#
# first = Rectangle(3, 6, 'red')
# first.set_color('blue')
# first.get_info()

# dz 22

# from math import sqrt
#
#
# class Pair:
#     def __init__(self, a, b):
#         self.A = a
#         self.B = b
#
#     def set_a(self, a):
#         self.A = a
#
#     def set_b(self, b):
#         self.B = b
#
#     def sum(self):
#         return self.A + self.B
#
#     def mult(self):
#         return self.A * self.B
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.C = self.hypot()
#
#     def hypot(self):
#         hypot = round(sqrt(self.A ** 2 + self.B ** 2), 2)
#         print(f"Гипотенуза АВС: {hypot}")
#         return hypot
#
#     def print_info(self):
#         print(f"Прямоугольный треугольник АВС ({self.A}, {self.B}, {self.C})")
#
#     def square(self):
#         s = round(0.5 * self.mult(), 2)
#         print(f"Площадь АВС: {s}")
#         return s
#
#
# tr = RightTriangle(5, 8)
# tr.print_info()
# tr.square()
# print()
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
# print()
# tr.set_a(10)
# tr.hypot()
# tr.set_b(20)
# tr.hypot()
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
# tr.square()


# Dz 23

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.NoteBook()
#
#     def display(self):
#         print(f"{self.name}", end=' ')
#         self.note.display()
#
#     class NoteBook:
#         def __init__(self):
#             self.hp = "HP"
#             self.i7 = "i7"
#             self.memory = "16"
#
#         def display(self):
#             print(f"=> {self.hp}, {self.i7}, {self.memory}")
#
#
# stud = Student("Roman")
# stud.display()
# stud2 = Student("Vladimir")
# stud2.display()

# dz 24 - 1

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec >= other.sec
#
#     def __lt__(self, other):
#         return not self.__gt__(other)
#
#     def __le__(self, other):
#         return not self.__ge__(other)
#
#
# c1 = Clock(600)
# c3 = Clock(700)
# if c3 > c1:
#     print("c3 > c1 True")
# else:
#     print("c3 < c1 False")
#
# if c3 >= c1:
#     print("c3 >= c1 True")
# else:
#     print("c3 <= c1 False")
#
# if c3 < c1:
#     print("c3 > c1 True")
# else:
#     print("c3 < c1 False")
# if c3 <= c1:
#     print("c3 >= c1 True")
# else:
#     print("c3 <= c1 False")
#
# # dz 24 - 2
#
#
# class Clock2:
#     __DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock2.__get_form(h)}:{Clock2.__get_form(m)}:{Clock2.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec % other.sec)
#
#     def __isub__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec - other.sec)
#
#     def __imul__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec * other.sec)
#
#     def __ifloordiv__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec // other.sec)
#
#     def __imod__(self, other):
#         if not isinstance(other, Clock2):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock2(self.sec % other.sec)
#
#
# c1 = Clock2(600)
# c2 = Clock2(200)
# print("c1:", c1.get_format_time())
# c3 = c1 - c2
# print("c1 - c2:", c3.get_format_time())
# c4 = c1 * c2
# print("c1 * c2:", c4.get_format_time())
# c5 = c1 // c2
# print("c1 // c2:", c5.get_format_time())
# c6 = c1 % c2
# print("c1 % c2:", c6.get_format_time())
# c1 -= c2
# print("c1 -= c2:", c1.get_format_time())
# c1 *= c2
# print("c1 *= c2:", c1.get_format_time())
# c1 //= c2
# print("c1 //= c2:", c1.get_format_time())
# c1 %= c2
# print("c1 %= c2:", c1.get_format_time())

# dz 25

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     def __init__(self, color, a):
#         self._color = color
#         self._a = a
#
#     def get_color(self):
#         return self._color
#
#     def set_color(self, color):
#         self._color = color
#
#     def get_a(self):
#         return self._a
#
#     def set_a(self, a):
#         self._a = a
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#     @abstractmethod
#     def get_square(self):
#         pass
#
#     @abstractmethod
#     def print_figure(self):
#         pass
#
#     @abstractmethod
#     def get_info(self):
#         pass
#
#
# class Square(Shape):
#
#     def get_perimeter(self):
#         return self._a * 4
#
#     def get_square(self):
#         return self._a * self._a
#
#     def print_figure(self):
#         return f'{"*" * self._a}\n' * self._a
#
#     def get_info(self):
#
#         print(f'===Квадрат==='
#               f'\nСторона : {self._a}'
#               f'\nЦвет: {self._color}'
#               f'\nПлощадь: {self.get_square()}'
#               f'\nПериметр: {self.get_perimeter()}'
#               f'\n{self.print_figure()}')
#
#
# class Rectangle(Square):
#     def __init__(self, color, a, b):
#         super().__init__(color, a)
#         self._b = b
#
#     def get_b(self):
#         return self._b
#
#     def set_b(self, b):
#         self._b = b
#
#     def get_perimeter(self):
#         return (self._a + self._b) * 2
#
#     def get_square(self):
#         return self._a * self._b
#
#     def print_figure(self):
#         a = self._a
#         b = self._b
#         if a < b:
#             a, b = b, a
#         return f'{"*" * a}\n' * b
#
#     def get_info(self):
#         print('===Прямоугольник==='
#               f'\nДлина: {self._a}'
#               f'\nШирина: {self._b}'
#               f'\nЦвет: {self._color}'
#               f'\nПлощадь: {self.get_square()}'
#               f'\nПериметр: {self.get_perimeter()}'
#               f'\n{self.print_figure()}')
#
#
# class Triangle(Rectangle):
#     def __init__(self, color, a, b, c):
#         super().__init__(color, a, b)
#         self.__c = c
#
#     def get_c(self):
#         return self.__c
#
#     def set_c(self, c):
#         self.__c = c
#
#     def get_perimeter(self):
#         return self._a + self._b + self.__c
#
#     def get_square(self):
#         p = self.get_perimeter() / 2
#         return round((p * (p - self._a) * (p - self._b) * (p - self.__c)) ** 0.5, 1)
#
#     def print_figure(self):
#         a = round((self._a + self._b) / 2)
#         c = self.__c
#         if c < a:
#             a, c = c, a
#         step = round(c / a)
#         prnt = ''
#         for i1 in range(a):
#             prnt += f'{" " * (step * (a - i1) // 2)}*{"*" * step * i1}\n'
#         return prnt
#
#     def get_info(self):
#         print(f'===Треугольник==='
#               f'\nСторона 1: {self._a}'
#               f'\nСторона 2: {self._b}'
#               f'\nСторона 3: {self.__c}'
#               f'\nЦвет: {self._color}'
#               f'\nПлощадь: {self.get_square()}'
#               f'\nПериметр: {self.get_perimeter()}'
#               f'\n{self.print_figure()}')
#
#
# lst = (Square('red', 3),
#        Rectangle('green', 3, 7),
#        Triangle('yellow', 6, 6, 11))
#
# for i in lst:
#     i.get_info()

# dz 27

# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#             'name': name,
#             'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])

# dz 28

# import csv
#
# with open("data2.csv") as r_file:
#     file_reader = csv.reader(r_file, delimiter=';')
#     for row in file_reader:
#         print(row)

# dz 29

# import csv
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open("dz29.csv", 'w') as f:
#         writer = csv.writer(f, delimiter=';')
#         writer.writerow((data['name']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     name = soup.find(id='post-10463').find('h1', class_='title-detail')
#
#     for i in name:
#         print(i.text)
#
#     data = {"name": name}
#     write_csv(data)
#
#
# def main():
#     url = "https://d23store.ru/10-samyh-populyarnyh-personazhej-garri-pottera-kotorye-voplotilis-v-vyazanyh-igrushkah-nashego-magazina-ruchnoj-raboty/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# dz 30

# from parsersdz30 import Parser
#
#
# def main():
#     pars = Parser("https://gifs.ru", "dz30.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# dz 35

# import sqlite3
#
# with sqlite3.connect("top-academy.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS students(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT NOT NULL,
#         name TEXT NOT NULL,
#         patronymic TEXT NOT NULL,
#         age INTEGER NOT NULL CHECK (age >= 16 AND age <= 45)
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS courses(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         course TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS records(
#         ID_st INTEGER NOT NULL,
#         ID_c INTEGER NOT NULL,
#         FOREIGN KEY (ID_st) REFERENCES students(id)
#         FOREIGN KEY (ID_c) REFERENCES courses(id)
#     )""")

# dz 39

from jinja2 import Template

html = """
{% macro set_input(type='', name='', placeholder='') -%}
    <input type="{{ type }}" name="{{ name }} placeholder="{{ placeholder }}" >
{%- endmacro -%}

<p>{{ set_input('text', 'firstname', 'Имя') }}</p>
<p>{{ set_input('text', 'lastname', 'Фамилия') }}</p>
<p>{{ set_input('text', 'address', 'Адрес') }}</p>
<p>{{ set_input('tel', 'phone', 'Телефон') }}</p>
<p>{{ set_input('email', 'email', 'Почта') }}</p>
"""

tm = Template(html)
msg = tm.render()
print(msg)
