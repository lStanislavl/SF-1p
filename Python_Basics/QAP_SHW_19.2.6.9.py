# Ваша задача — протестировать модули, которые отвечают за генерацию паролей для пользователей.
# Вам нужно создать замыкание, которое будет генерировать уникальные пароли заданной длины из заданных символов,
# чтобы убедиться в его эффективности и безопасности.
# Создайте замыкание create_password_generator, которое будет генерировать пароль указанной длины из заданных символов.
# При каждом вызове должен генерироваться новый уникальный пароль.
# create_password_generator принимает целое число — длину генерируемого пароля, и symbols — строку из символов,
# которые будут участвовать в генерации пароля.
# Примечание: в качестве отправки ответа на проверку нужно только объявить 'create_password_generator'.

import random

def create_password_generator(length, symbols):
    used_passwords = set()

    def generator():
        nonlocal used_passwords
        while True:
            password = ''.join(random.choice(symbols) for _ in range(length))
            if password not in used_passwords:
                used_passwords.add(password)
                return password

    return generator