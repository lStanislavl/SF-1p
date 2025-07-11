# Cистемы, отслеживающей транзакции пользователей. Вы заметили, что система должна уметь проверять
# уникальность идентификаторов транзакций.
# Задача – Вам нужно создать замыкание, которое будет проверять, встречалось ли значение ранее или нет.
# Вам необходимо проверять уникальность элементов. Создайте замыкание — функцию create_unique_checker, —
# которое принимает значение и возвращает True, если это значение ранее не встречалось, и False в противном случае.

def create_unique_checker():
    seen = set()

    def checker(value):
        if value in seen:
            return False
        else:
            seen.add(value)
            return True

    return checker