# Вам нужно создать классы, которые будут представлять разные типы объектов недвижимости,
# а также класс агентства, который будет отвечать за управление списком доступных объектов.
# Базовый класс SellItem:
# Инициализатор, который устанавливает локальные свойства:
# name: строка;
# price: целое или дробное число;
# Дочерний класс House класса SellItem:
# Инициализатор, который устанавливает локальные свойства:
# name: строка (установка должна осуществляться инициализатором базового класса);
# price: целое или дробное число (установка должна осуществляться инициализатором базового класса);
# material: строка;
# square: целое или дробное число.
# Дочерний класс Flat класса SellItem:
#
# Инициализатор, который устанавливает локальные свойства:
# name: строка (установка должна осуществляться инициализатором базового класса)
# price: целое или дробное число (установка должна осуществляться инициализатором базового класса)
# size: целое или дробное число
# rooms: целое или дробное число
# Класс Agency:
#
# Инициализатор, который устанавливает локальные свойства:
# name: строка
# objs: пустой список (не передаётся в качестве аргумента инициализатору)
# Метод add_object() добавляет переданный объект в список objs
# Метод remove_object() удаляет переданный объект из списка objs
# Метод get_objects() возвращает свойство objs.

class SellItem:
    def __init__(self, name: str, price):
        self.name = name
        self.price = price

class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Agency:
    def __init__(self, name):
        self.name = name
        self.objs = []

    def add_object(self, obj):
        self.objs.append(obj)

    def remove_obj(self, obj):
        self.objs.remove(obj)

    def get_objects(self):
        return self.objs
