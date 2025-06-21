# При разработке сервиса охраны бизнес-центра вам поручили реализовать класс Person для
# создания пропускных карточек.
# В этом классе инициализатор __init__() должен принимать аргументы:
# - name;
# - age;
# - gender;
# - occupation.
#
# В качестве значения по умолчанию у этих аргументов должно быть None. Также __init__() должен
# создавать локальные свойства в экземпляре с соответствующими именами.
#
# Реализуйте методы:
# - set_attributes(), который принимает словарь с произвольным числом записей, которые
# представлены в нём в виде имя_атрибута: значение и которые вам необходимо обновить в классе
# (в словаре может быть произвольное значение записей, например только для name и age).
# - show_card(), который выводит строку (многострочную) следующего вида:
#
# Name: значение_атрибута_name
# Age: значение_атрибута_age
# Gender: значение_атрибута_gender
# Occupation: значение_атрибута_occupation

class Person:
   def __init__(self):
       self.name = None
       self.age = None
       self.gender = None
       self.occupation = None

   def set_attributes(self, attr_dict):
       if 'name' in attr_dict:
           self.name = attr_dict['name']
       if 'age' in attr_dict:
           self.age = attr_dict['age']
       if 'gender' in attr_dict:
           self.gender = attr_dict['gender']
       if 'occupation' in attr_dict:
           self.occupation = attr_dict['occupation']

   def show_card(self):
       print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}")
