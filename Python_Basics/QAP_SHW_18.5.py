todo_list = [['',    '',    ''],
             ['',    '',    ''],
             ['',    '',    ''],
             ['',    '',    ''],
             ['',    '',    ''],
             ['',    '',    ''],
             ['',    '',    ''],]
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
time = ['утро', 'день', 'вечер']

print('Заполнить ежедневник')
for i in range(7):
   for j in range(3):
      print(days[i], time[j])
      task = input('Введите дело: ')
      todo_list[i][j] = task

print()
print('Удалить запись: ')
i = int(input('Введите индекс дня недели: '))
j = int(input('Введите индекс времени дня: '))
todo_list[i].pop(j)

print()
print('Добавить запись: ')
i = int(input('Введите индекс дня недели: '))
task = input('Введите дело: ')
todo_list[i].append(task)

print()
print('Итоговый список дел: ')
for i in range(7):
   print(days[i])
   print(todo_list[i])
   print()