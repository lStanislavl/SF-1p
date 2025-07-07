# Напишите функцию test_case_generator(), которая возвращает вложенную функцию run_test(test).
# Эта вложенная функция должна:
# Увеличивать глобальные переменные tests_run и tests_failed для отслеживания количества выполненных и
# проваленных тестов.
# Увеличивать на единицу и возвращать уникальный идентификатор тест-кейса при каждом вызове.
# Принимать тестовую функцию test, запускать ее и обновлять количество проваленных тестов, если тест не проходит.
# Задача – Здесь вам по сути необходимо объединить решения из двух предыдущих заданий.

tests_run = 0
tests_failed = 0

def test_case_generator():
    case_id = 0

    def run_test(test):
        nonlocal case_id
        global tests_run
        global tests_failed
        tests_run += 1
        if not test():
            tests_failed += 1
        case_id += 1
        return case_id

    return run_test