# С помощью рекурсии определите, является ли слово палиндромом.
# Для этого реализуйте функцию is_palindrome, которая принимает строку s.
# Если слово — палиндром, функция должна возвращать True, если не палиндром — False.

def is_palindrome(s):
   if len(s) < 2:
       return True
   if s[0] != s[-1]:
       return False
   return is_palindrome(s[1:-1])