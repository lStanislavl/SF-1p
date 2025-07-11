# Вы — разработчик программного обеспечения в стартапе, который создаёт продукт управления задачами.
# Ваша команда хочет, чтобы вы разработали прототип системы управления задачами на языке Python.
# Для этого вам необходимо создать класс TaskList, который содержит инициализатор, который, в свою очередь,
# инициализирует приватное свойство task_list пустым списком.
# В процессе работы программы список task_list будет наполняться элементами — задачами (task).
# task — словарь вида {'name': str, 'done': bool}, где ключ done при дальнейшей реализации будет говорить о
# статусе её выполнения.
# Метод add_task() должен добавлять задачу в список, проверяя, есть ли уже такая задача в списке и выводя
# строки "Задача <name> добавлена в список" и "Задача <name>  уже есть в списке" соответственно.
# Метод remove_task() должен принимать название задачи и удалять эту задачу (соответствующий словарь) из списка,
# проверяя, существует ли такая задача, выводя при этом на экране соответствующие сообщения:
# "Задача <название_задачи> удалена из списка" или "Задачи <название_задачи> нет в списке".
# Вспомогательный приватный метод is_task_in_list() должен проверять, существует ли такая задача в списке и
# возвращать значение True или False соответственно.

class TaskList:
    def __init__(self):
        self.__task_list = []

    def __is_task_in_list(self, task):
        for t in self.__task_list:
            if t['name'] == task:
                return True
        return False

    def add_task(self, task):
        if not self.__is_task_in_list(task):
            self.__task_list.append({'name': task, 'done': False})
            print(f'Задача "{task}" добавлена в список')
        else:
            print(f'Задача "{task}" уже есть в списке')

    def remove_task(self, task_name):
        for task in self.__task_list:
            if task['name'] == task_name:
                self.__task_list.remove(task)
                print(f'Задача "{task_name}" удалена из списка')
                return
        print(f'Задачи "{task_name}" нет в списке')
