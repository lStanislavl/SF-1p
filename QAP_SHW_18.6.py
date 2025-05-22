contacts = {}
for i in range(4):
    name = input('Введите имя: ')
    phone = input('Введите номер: ')
    contacts[name] = phone
print(contacts.keys())
print(contacts.values())

print()
for name, phone in contacts.items():
    print(f'Контакт: {name} Телефон: {phone}')

print('Добавить новую запись в телефонную книгу: ')
for i in range(2):
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    contacts[name] = phone
    print('Запись добавлена в телефонную книгу')

print('Редактировать запись в телефонной книге:')
print(contacts)
name = input('Введите имя из телефонной книги: ')
phone = input('Введите новый номер телефона: ')
contacts[name] = phone
print('Запись отредактирована')

print('Проверить наличие записи в телефонной книге:')
name = input('Введите имя: ')
if name in contacts.keys():
    del contacts[name]
    print('Запись удалена')
else:
    phone = input('Введите номер телефона: ')
    contacts[name] = phone
    print('Запись добавлена в телефонную книгу')

print(contacts)