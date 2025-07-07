coworkers = ['Stanislav', 'Oleg', 'Svetlana', 'Alexsandra', 'Julia', 'Igor']
print(f'''Первый элемент списка {coworkers[0]} Последний элемент списка {coworkers[-1]}''')
print(coworkers[::2])
print(coworkers[1::2])
print(f'Длина списка: {len(coworkers)}')
name = input('Введите имя нового коллеги: ')
coworkers.append(name)
print(f'Длина списка: {len(coworkers)}')
name = input('Введите имя коллеги: ')
if name in coworkers:
    print('Этот коллега есть в списке')
else:
    print('Такого имени в списке нет')