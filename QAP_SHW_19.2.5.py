# Напишите функцию check_password, которая принимает пароль в виде строки и проверяет, что:
#
# длина пароля не менее 8 символов;
# в пароле есть хотя бы одна заглавная буква;
# в пароле есть хотя бы одна строчная буква;
# в пароле есть хотя бы одна цифра.
# Функция должна выводить сообщение, если пароль не соответствует какому-либо из этих условий.

def check_password(password):
   if len(password) < 8:
       print("Пароль должен быть не менее 8 символов")
   upper, lower, digit = False, False, False
   for char in password:
       if char.isupper():
           upper = True
       elif char.islower():
           lower = True
       elif char.isdigit():
           digit = True
   if not upper:
       print("Пароль должен содержать хотя бы одну заглавную букву")
   if not lower:
       print("Пароль должен содержать хотя бы одну строчную букву")
   if not digit:
       print("Пароль должен содержать хотя бы одну цифру")