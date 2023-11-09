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

#dz 22

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

class Clock:
    __DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec >= other.sec

    def __lt__(self, other):
        return not self.__gt__(other)

    def __le__(self, other):
        return not self.__ge__(other)


c1 = Clock(600)
c3 = Clock(700)
if c3 > c1:
    print("c3 > c1 True")
else:
    print("c3 < c1 False")

if c3 >= c1:
    print("c3 >= c1 True")
else:
    print("c3 <= c1 False")

if c3 < c1:
    print("c3 > c1 True")
else:
    print("c3 < c1 False")
if c3 <= c1:
    print("c3 >= c1 True")
else:
    print("c3 <= c1 False")

# dz 24 - 2


class Clock2:
    __DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock2.__get_form(h)}:{Clock2.__get_form(m)}:{Clock2.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec % other.sec)

    def __isub__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec - other.sec)

    def __imul__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec * other.sec)

    def __ifloordiv__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec // other.sec)

    def __imod__(self, other):
        if not isinstance(other, Clock2):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock2(self.sec % other.sec)


c1 = Clock2(600)
c2 = Clock2(200)
print("c1:", c1.get_format_time())
c3 = c1 - c2
print("c1 - c2:", c3.get_format_time())
c4 = c1 * c2
print("c1 * c2:", c4.get_format_time())
c5 = c1 // c2
print("c1 // c2:", c5.get_format_time())
c6 = c1 % c2
print("c1 % c2:", c6.get_format_time())
c1 -= c2
print("c1 -= c2:", c1.get_format_time())
c1 *= c2
print("c1 *= c2:", c1.get_format_time())
c1 //= c2
print("c1 //= c2:", c1.get_format_time())
c1 %= c2
print("c1 %= c2:", c1.get_format_time())
