import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Добавить ученика
        5. Удалить ученика
        6. Изменить имя ученика
        7. Изменить оценку ученика по предмету
        8. Удалить оценку ученика по предмету
        9. Добавить предмет
        10. Удалить предмет
        11. Изменить название предмета
        12. Вывести все оценки ученика
        13. Средний балл ученика по каждому предмету
        14. Вывести список учеников
        15. Вывести список предметов
        16. Вывести список отстающих учеников по одному предмету
        17. Вывести список преуспевающих учеников по одному предмету
        18. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))

    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print('4. Добавить ученика')
        student = input('Введите имя нового ученика: ')
        if student in students:
            print('ОШИБКА: такой ученик уже есть в списке')
        else:
            students.append(student)
            students_marks[student] = {}
            for class_ in classes:
                marks = [random.randint(1, 5) for i in range(3)]
                students_marks[student][class_] = marks
            students.sort()
            print(f'Список учеников: {students}')

    elif command == 5:
        print('5. Удалить ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            del students_marks[student]
            students.remove(student)
            print(f'Студент {student} был удален')
            students.sort()
            print(f'Список учеников: {students}')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 6:
        print('6. Изменить имя ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            student_new = input('Введите новое имя ученика: ')
            students.append(student_new)
            students_marks[student_new] = students_marks[student]
            students.remove(student)
            print(f'Имя изменено')
            print(f'Список учеников: {students}')
        else:
            print('ОШИБКА: такого ученика нет в списке')

    elif command == 7:
        print('7. Изменить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            mark = int(input('Введите оценку: '))
            if mark in students_marks[student][class_]:
                mark_new = int(input('Введите новую оценку: '))
                students_marks[student][class_].append(mark_new)
                students_marks[student][class_].remove(mark)
                print('Оценка изменена')
            else:
                print('ОШИБКА: такой оценки нет в списке')
        else:
            print('ОШИБКА: неверное имя ученика или предмета')

    elif command == 8:
        print('8. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            mark = int(input('Введите оценку: '))
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print('Оценка удалена')
            else:
                print('ОШИБКА: такой оценки нет в списке')
        else:
            print('ОШИБКА: неверное имя ученика или предмета')

    elif command == 9:
        print('9. Добавить предмет')
        class_ = input('Введите имя нового предмета: ')
        if class_ in classes:
            print('ОШИБКА: такой предмет уже существует')
        else:
            classes.append(class_)
            for student in students:
                for class_ in classes:
                    marks = [random.randint(1, 5) for i in range(3)]
                    students_marks[student][class_] = marks
            print('Предмет добавлен')

    elif command == 10:
        print('10. Удалить предмет')
        class_ = input('Введите имя предмета: ')
        if class_ in classes:
            classes.remove(class_)
            print('Предмет удален')
        else:
            print('ОШИБКА: такого предмета не существует')

    elif command == 11:
        print('11. Изменить название предмета')
        class_ = input('Введите название предмета: ')
        if class_ in classes:
            class_new = input('Введите новое название предмета: ')
            classes.append(class_new)
            for student in students:
                students_marks[student][class_new] = students_marks[student][class_]
            classes.remove(class_)
            print(f'Название изменено')
        else:
            print('ОШИБКА: такого предмета нет в списке')

    elif command == 12:
        print('12. Вывести все оценки ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
        else:
            print('ОШИБКА: такого ученика нет в списке')

    elif command == 13:
        print('13. Средний балл ученика по каждому предмету')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
        else:
            print('ОШИБКА: такого ученика нет в списке')

    elif command == 14:
        print('14. Вывести список учеников')
        print(students)

    elif command == 15:
        print('15. Вывести список предметов')
        print(classes)

    elif command == 16:
        print('16. Вывести список отстающих учеников по одному предмету')
        class_ = get_class_ = input("Введите предмет, по которому нужно вывести список отстающих учеников: ")
        if not class_:
            continue
        print(f"Список отстающих учеников по предмету {class_} (средний балл < 3):")
        for student in students:
            if class_ in students_marks[student]:
                marks = students_marks[student][class_]
                if marks:
                    average = sum(marks) / len(marks)
                    if average < 3:
                        print(f" {student}: {average:.2f}")
                else:
                    print(f" {student}: Нет оценок")
            else:
                print(f" {student}: Нет данных по этому предмету")

    elif command == 17:
        print('17. Вывести список преуспевающих учеников по одному предмету')
        class_ = get_class_ = input("Введите предмет, по которому нужно вывести список преуспевающих учеников: ")
        if not class_:
            continue
        print(f"Список преуспевающих учеников по предмету {class_} (средний балл >= 4):")
        for student in students:
            if class_ in students_marks[student]:
                marks = students_marks[student][class_]
                if marks:
                    average = sum(marks) / len(marks)
                    if average >= 4:
                        print(f" {student}: {average:.2f}")
                else:
                    print(f" {student}: Нет оценок")
            else:
                print(f" {student}: Нет данных по этому предмету")

    elif command == 18:
        print('18. Выход из программы')
        break

    else:
        print('Неверная команда.')