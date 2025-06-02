# В этом задании вам предстоит усовершенствовать функцию проверки пароля, добавив в неё значения по умолчанию,
# которыми будет определяться необходимость проверки того или иного параметра пароля.
# Напишите функцию is_valid_password(), которая принимает пароль в виде строки и проверяет его на соответствие
# следующим критериям:

# Длина не менее 8 символов;
# есть хотя бы одна заглавная буква;
# есть хотя бы одна строчная буква;
# есть хотя бы одна цифра.

# Функция должна иметь параметры по умолчанию, определяющие требования к паролю,
# чтобы можно было настроить проверку в соответствии с потребностями безопасности:
# min_length=8, require_upper=True, require_lower=True, require_digit=True.

def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
   if len(password) < min_length:
       return False
   has_upper = False
   has_lower = False
   has_digit = False
   for char in password:
       if char.isupper():
           has_upper = True
       if char.islower():
           has_lower = True
       if char.isdigit():
           has_digit = True
   if require_upper and not has_upper:
       return False
   if require_lower and not has_lower:
       return False
   if require_digit and not has_digit:
       return False
   return True