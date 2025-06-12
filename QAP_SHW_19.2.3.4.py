# Для генерирования тестовых наборов данных вам необходимо создать функцию-генератор generate_user_data,
# которая принимает: размер генерируемой последовательности, список возможных имен, список возможных фамилий,
# диапазон возраста (список из двух чисел, включительно).
#
# Генерируемые значения — кортеж из имени, фамилии и возраста.
# Данные значения должны генерироваться случайным образом (воспользуйтесь библиотекой random).

import random
def generate_user_data(count, first_names, last_names, age_diapason):
   for _ in range(count):
       name = random.choice(first_names)
       surname = random.choice(last_names)
       age = random.randint(age_diapason[0], age_diapason[1])
       yield name, surname, age