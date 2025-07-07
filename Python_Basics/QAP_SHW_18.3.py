from os import remove
from urllib.response import addbase

family = ('Stanislav', 'Alexsandra','Oleg', 'Svetlana', 'Igor', 'Julia')
print(f'''Первый элемент: {family[0]} 
Последний элемент: {family[-1]}''')
print(family[1::2])



numbers = set([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9])
num = int(input('Введите число: '))
if num in numbers:
    print('Удаляем число из множества')
    numbers.remove(num)
else:
    print('Добавляем число во множество')
    numbers.add(num)
print(f'Длина множества: {len(numbers)}')
print(numbers)