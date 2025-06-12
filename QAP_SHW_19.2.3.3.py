# Во многих веб-приложениях URL-ы могут быть структурированы последовательно
# (например, /product/1, /product/2 и так далее). Создайте функцию-генератор generate_urls,
# которая будет возвращать последовательные URL-ы для заданного шаблона и диапазона чисел.

def generate_urls(base_url, start, end):
   for i in range(start, end + 1):
       yield f"{base_url}{i}"