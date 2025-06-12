# Дан список багов, где каждый баг представлен в виде словаря со следующими ключами:
# id, description, severity. severity может быть одним из трех значений: "low", "medium", "high".
# Напишите функцию filter_high_severity, которая принимает список багов и возвращает список багов только с
# высокой степенью серьезности ("high").

def filter_high_severity(bugs):
   return list(filter(lambda bug: bug["severity"] == "high", bugs))