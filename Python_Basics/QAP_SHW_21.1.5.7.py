# Мы разрабатываем приложение, которое подразумевает функционал авторизации пользователя,
# а также управление его балансом на некотором виртуальном счете. Определите класс для пользователей
# User.
# У него должны быть:
# атрибуты email, password и balance, которые устанавливаются при инициализации в методе __init__();
# метод login(), который реализует проверку почты и пароля. Метод должен принимать в
# качестве аргументов емайл (email) и пароль (password). Если они совпадают с атрибутами объекта,
# он возвращает True, а иначе — False;
# метод update_balance(), который должен принимать в качестве аргумента amount некоторое
# число и изменять текущий баланс счёта (атрибут balance) на величину amount.

class User():
    def __init__(self, email, password, balance):
        self.email=email
        self.password=password
        self.balance=balance

    def login(self, email, password):
        if self.email==email and self.password==password:
            answer=True
        else:
            answer=False
        return answer

    def update_balance(self, amount):
        self.balance+=amount
        return self.balance
