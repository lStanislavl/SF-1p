# Вы проводите автоматическое тестирование времени ответа сервера.
# Вам необходимо написать функцию calculate_average(*args), которая принимает список времени ответа и
# возвращает среднее значение.

def calculate_average(*args):
   return sum(args) / len(args)