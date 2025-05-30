# Напишите функцию is_success_code(), которая принимает код ответа HTTP и возвращает True,
# если это код успешного ответа (в диапазоне 200-299), и False в противном случае.
# Передаваемое значение имеет имя code

def is_success_code(code):
   if 200 <= code <= 299:
       return True
   else:
       return False