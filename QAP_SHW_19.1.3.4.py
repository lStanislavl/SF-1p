# Напишите функцию is_valid_email(), которая принимает email в виде строки и возвращает True, если email:
#
# содержит символ "@";
# содержит хотя бы одну точку после символа "@";
# не содержит пробелов.
# В противном случае функция должна возвращать False.

def is_valid_email(email):
   if " " in email:
       return False
   at_index = email.find("@")
   if at_index == -1:  # символ "@" отсутствует
       return False
   if "." not in email[at_index:]:  # после "@" отсутствует "."
       return False
   return True