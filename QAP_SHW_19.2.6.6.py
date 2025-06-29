# Вы приступаете к тестированию функционала, который отслеживает, сколько раз пользователи выполняют определенные
# действия в приложении. Вам нужно создать замыкание-счетчик, которое поможет вам в этой задаче.
# Для этого создайте функцию create_counter, которая возвращает замыкание-счетчик.
# Счетчик должен увеличиваться на 1 каждый раз, когда вызывается замыкание.

def create_counter():
    count = 0

    def counter():
            nonlocal count
            count += 1
            return count

    return counter