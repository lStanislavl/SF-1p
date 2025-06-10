# У вас есть данные об активности пользователей в формате словаря, где ключ — идентификатор пользователя,
# а значение — количество его активностей.
#
# Напишите функцию sort_users_by_activity, которая будет возвращать список пользователей,
# отсортированных по уровню активности в порядке убывания. Функция sorted должна использоваться с аргументом key и
# лямбда-функцией.

def sort_users_by_activity(user_activity):
   sorted_users = sorted(user_activity.items(), key=lambda x: x[1], reverse=True)
   return [user[0] for user in sorted_users]