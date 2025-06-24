# Ваша задача — реализовать систему принятия и выполнения заказов в ресторане с использованием очереди.

class Order:
    # Конструктор класса Order, который инициализирует новый заказ.
    def __init__(self, customer_name, dishes):
        self.customer_name = customer_name  # Имя клиента, сделавшего заказ.
        self.dishes = dishes  # Список блюд в заказе.
        self.status = "новый"  # Начальный статус заказа.


class RestaurantQueue:
    def __init__(self):
        self.queue = []  # Список заказов

    # Метод проверяет, пуста ли очередь заказов.
    def is_empty(self):
        return len(self.queue) == 0

    # Метод добавляет заказ в конец очереди.
    def add_order(self, order):
        self.queue.append(order)  # Добавление заказа в очередь.
        print(f"Заказ от {order.customer_name} добавлен в очередь.")

    # Метод извлекает и возвращает первый заказ из очереди, меняя его статус.
    def take_order(self):
        if not self.is_empty():
            order = self.queue.pop(0)  # Извлечение заказа из очереди.
            order.status = "в процессе"  # Изменение статуса заказа.
            print(f"Заказ от {order.customer_name} взят в работу.")
            return order
        else:
            print("Очередь заказов пуста.")
            return None

    # Метод отмечает переданный заказ как выполненный.
    def complete_order(self, order):
        order.status = "готов"
        print(f"Заказ от {order.customer_name} готов.")

    # Метод выводит информацию о текущих заказах в очереди.
    def print_queue(self):
        if self.is_empty():
            print("Очередь заказов пуста.")
        else:
            print("Текущие заказы:")
            for i, order in enumerate(self.queue):
                print(f"{i + 1}. Заказ от {order.customer_name} ({order.status})")

# Пример использования
queue = RestaurantQueue()

order1 = Order("Иван", ["пицца", "салат"])
order2 = Order("Мария", ["суп", "стейк"])

queue.add_order(order1)
queue.add_order(order2)

queue.print_queue()

order_in_progress = queue.take_order()

queue.print_queue()

queue.complete_order(order_in_progress)