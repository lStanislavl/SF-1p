# Проверить, что число попадает в определённый диапазон.

def test_range(number, range_start, range_end):
   if not (range_start <= number <= range_end):
       print("Число {} не попадает в диапазон между {} и {}".format(number, range_start, range_end))