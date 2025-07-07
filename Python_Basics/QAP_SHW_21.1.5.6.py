# Вы участвуете в разработке онлайн-магазина. Вам необходимо реализовать класс Queue (очередь),
# чтобы обрабатывать заказы в порядке их поступления.
# Инициализатор этого класса должен создавать атрибут items — пустой список.
#
# Реализуйте в классе методы:
# - enqueue() — принимает один аргумент (идентификатор заказа) и добавляет его в конец списка items.
# - is_empty() — возвращает True, если очередь пуста, и False — в противном случае.
# - dequeue() — удаляет первый элемент списка items и возвращает его.
# - show_queue() — выводит элементы списка items на экран в одну строку через пробел.

class Queue:
   def __init__(self):
       self.items = []

   def enqueue(self, item):
       self.items.append(item)

   def dequeue(self):
       if not self.is_empty():
           return self.items.pop(0)

   def is_empty(self):
       return len(self.items) == 0

   def show_queue(self):
       print(*self.items)
