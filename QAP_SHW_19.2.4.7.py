# У вас есть список с результатами тестовых кейсов.
# Каждый результат может быть одним из следующих значений: "pass", "fail", "skip". Напишите две функции:
#
# • has_failures(test_results): функция должна вернуть True, если хотя бы один из тестовых кейсов
# завершился с результатом "fail", иначе False.
# • all_passed_or_skipped(test_results): функция должна вернуть True, если все тестовые кейсы
# завершились с результатом "pass" или "skip", иначе False.

def has_failures(test_results):
   return any(result == "fail" for result in test_results)

def all_passed_or_skipped(test_results):
   return all(result in ["pass", "skip"] for result in test_results)