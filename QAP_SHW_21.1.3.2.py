# При дальнейшей разработке платформы онлайн-школы вам поручили дополнить логику программы возможностью объединения
# студентов в группы. Для этого объявите класс Group с атрибутом members, который ссылается на пустой список.
# Также объявите класс Student и создайте студента s1 в соответствии с предыдущим заданием. Далее создайте студента s2.
#
# Значения атрибутов для s1:
# name = 'Иван'
# surname = 'Иванов'
# semester = 1
#
# Значения атрибутов для s2:
# name = 'Лев'
# surname = 'Сергеев'
# semester = 1
# После этого обратитесь к значению атрибута members класса Group и добавьте в список объекты s1 и s2.
# Запишите в переменную result значение атрибута members класса Group.

class Group:
   members = []


class Student:
   course = 'Data Science'


s1 = Student()
s1.name = 'Иван'
s1.surname = 'Иванов'
s1.semester = 1

s2 = Student()
s2.name = 'Лев'
s2.surname = 'Сергеев'
s2.semester = 1

Group.members.append(s1)
Group.members.append(s2)

result = Group.members
