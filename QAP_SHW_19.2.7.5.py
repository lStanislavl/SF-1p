# Создайте декоратор time_it, который будет измерять и выводить время выполнения функции строкой вида
# "Function {имя функции} took {время в секундах} seconds to run".
# При этом время переводите в целое перед передачей в строку
# (не пугайтесь времени выполнения = 0.0 секунд в случае округления).

import time

def time_it(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function {func.__name__} took {int(end - start)} seconds to run")
    return wrapper