# Создайте функцию process_test_data(*args, **kwargs), которая принимает данные тестового кейса
# в виде аргументов и возвращает их в виде строки, где данные разделены запятыми.

def process_test_data(*args, **kwargs):
   args_str = ', '.join(str(arg) for arg in args)
   kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
   return ', '.join([args_str, kwargs_str])