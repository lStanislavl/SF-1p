# Ваша команда QA создает автоматизированные тесты для нового API, который принимает различные параметры.
# Вам нужно написать функцию check_data_format(**kwargs), которая будет проверять,
# что все переданные аргументы в формате ключ-значение соответствуют условию:
# ключ это строка, значение это число.

def check_data_format(**kwargs):
   for key, value in kwargs.items():
       if type(key) != str or not (type(value) == int or type(value) == float):
           return False
   return True