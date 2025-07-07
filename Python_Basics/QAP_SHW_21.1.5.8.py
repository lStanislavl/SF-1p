# Определите класс IntDataFrame, который в момент инициализации объектов принимает список
# неотрицательных чисел и приводит к целым значениям все числа в этом списке, отрезая
# дробную часть с помощью встроенной функции int().
# Результирующий список должен быть сохранен в виде атрибута с именем column.
# Также класс должен содержать следующие методы:
# count(), который возвращает количество ненулевых элементов в списке column;
# unique(), который возвращает число уникальных элементов в списке в списке column.

class IntDataFrame():
    def __init__(self, column):
        self.column = list(map(lambda x: int(x), column))

    def count(self):
        return len(list(filter(lambda x: x!=0, self.column)))

    def unique(self):
        return len(set(self.column))
