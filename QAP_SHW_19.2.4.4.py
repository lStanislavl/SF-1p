# Дан список тестовых кейсов, где каждый тестовый кейс представлен в виде словаря со следующими ключами:
# id, description, type. type может быть одним из следующих значений: "UI", "API", "Performance".
# Напишите функцию, которая принимает список тестовых кейсов и возвращает только тестовые кейсы типа "API".

def filter_api_tests(test_cases):
   return list(filter(lambda test_case: test_case["type"] == "API", test_cases))