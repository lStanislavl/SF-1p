# Ваша задача — реализовать декоратор, который должен обрабатывать определённые ошибки.
# Создайте декоратор handle_exceptions, который будет обрабатывать исключения и выводить их
# в консоль — строку вида "Function {имя функции} raised an exception: {сообщение из ошибки}"

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Function {func.__name__} raised an exception: {e}")
    return wrapper