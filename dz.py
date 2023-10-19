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
class Car:
    model = ""
    year = "0"
    manufacturer = ""
    engine_volume = "0.0"
    color = ""
    price = "0.0"

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(
            f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\nМощность двигателя: {self.engine_volume}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def set_model(self, model):  # Устанавливает значение
        self.model = model

    def get_model(self):  # получает значение
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def get_engine_volume(self):
        return self.engine_volume

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


car = Car()
car.input_info("X7 M50i", 2021, "BMW", "530 л.с.", "white", 10790000)
car.print_info()
car.set_model("Q8")
print(car.get_model())
car.set_year("2021")
print(car.get_year())
car.set_manufacturer("Audi")
print(car.get_manufacturer())
car.set_engine_volume("440 л.с.")
print(car.get_engine_volume())
car.set_color("blue")
print(car.get_color())
car.set_price("7800000")
print(car.get_price())

