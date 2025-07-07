# Ваша задача: Создайте декоратор ensure_result_is_number, который будет возвращать None,
# если значение функции не является числом, иначе — возвращать результат работы функции.

import random

def ensure_result_is_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return result
        else:
            return None
    return wrapper