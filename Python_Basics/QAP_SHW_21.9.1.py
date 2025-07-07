# Ваша цель — создать простую систему для учебного процесса, где ученики получают оценки, а учебный персонал
# их классифицирует.
# В нашей системе уже есть класс Student. С его реализацией вы можете познакомиться в шаблоне задания.
# От вас требуется создать базовый класс Mentor, а также два дочерних по отношении к нему класса: Lector и Reviewer.
# Объявите класс Mentor, внутри инициализатора которого создаются свойства fio и subject.
# Добавьте в класс абстрактный метод set_mark(), который принимает аргументы:
# - student — ссылку на объект класса Student; - mark — оценку для этого студента.
# Метод должен быть абстрактным и должен выбрасывать исключение NotImplementedError (без пояснительной строки).
# Объявите дочерний по отношении классу Mentor класс Lector.
# - Переопределите в нём метод set_mark() — лектор ставит студентам оценки за лекции. - Также определите метод __str__(), чтобы он возвращал строку «Лектор <фио>: предмет <предмет>». Объявите дочерний по отношении классу Mentor класс Reviewer.
# - Переопределите в нём метод set_mark() — эксперт ставит студентам оценки за домашнюю работу. - Также определите метод __str__(), чтобы он возвращал строку «Эксперт <фио>: предмет <предмет>».
# Для корректной проверки ваше решение должно включать объявление класса Student, его код оставьте неизменным.

class Student:
    def __init__(self, fio, group):
        self.fio = fio  # ФИО студента (строка)
        self.group = group  # группа (строка)
        self.lect_marks = []  # оценки за лекции
        self.homework_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self.lect_marks.append(mark)

    def add_homework_marks(self, mark):
        self.homework_marks.append(mark)

    def __str__(self):
        return f"Студент {self.fio}: оценки на лекциях: {str(self.lect_marks)}; оценки за д/з: {str(self.homework_marks)}"

class Mentor():
    def __init__(self, fio, subject):
        self.fio = fio
        self.subject = subject

    def set_mark(self, student, mark):
        raise NotImplementedError

class Lector(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f"Лектор {self.fio}: предмет {self.subject}"

class Reviewer(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_homework_marks(mark)

    def __str__(self):
        return f"Эксперт {self.fio}: предмет {self.subject}"
