# В этом задании вам необходимо реализовать функцию compare_lists(), которая принимает два списка и возвращает
# список элементов, которые есть в первом списке, но отсутствуют во втором.
# Функция должна иметь параметр по умолчанию ignore_case=False,
# который позволяет игнорировать регистр при сравнении строк.

def compare_lists(list1, list2, ignore_case=False):
   if ignore_case:
       list2 = [item.lower() for item in list2]
       return [item for item in list1 if item.lower() not in list2]
   else:
       return [item for item in list1 if item not in list2]