# Чтобы усовершенствовать тестирование, реализуйте следующий набор функций:
#
# • convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]: Функция преобразует список словарей с данными
# о пользователях в список строк с полными именами. В контексте тестирования можно использовать эту функцию
# для проверки, что данные о пользователях правильно преобразуются перед отображением на веб-странице.

# • find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set: Функция находит
# уникальные имейлы, которые есть и в первом, и во втором списке пользователей.
# В контексте тестирования можно использовать эту функцию для проверки, что два списка пользователей
# корректно объединяются, и находятся только уникальные имейлы.

# • combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]: Функция объединяет данные о пользователях
# из разных списков в один словарь, где ключами будут поля из словарей, а значениями — списки соответствующих
# значений полей. В контексте тестирования можно использовать эту функцию для проверки, что данные о пользователях
# правильно объединяются перед обновлением в базе данных приложения.

from typing import List, Dict, Any
from functools import reduce

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    full_names = list(map(lambda user: f"{user['first_name']} {user['last_name']}", users))
    return full_names

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    emails1 = set(map(lambda user: user['email'], users1))
    emails2 = set(map(lambda user: user['email'], users2))
    matching_emails = emails1.intersection(emails2)
    return matching_emails

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    keys = users[0].keys()
    combined_data = dict(zip(keys, zip(*[user.values() for user in users])))
    return combined_data
