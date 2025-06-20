import json

data = {
'translator' :
    {
    'bugs':'ошибка',
    'function':'функция',
    'approve':'согласовать'
    },
1:'int key',
'set':(0, 1, 2, 3),
'empty value':None
}

with open("data.json", "w") as my_file:
    json.dump(data, my_file)

with open("data.json", "r") as my_file:
    data_json = my_file.read()
data = json.loads(data_json)
print(data_json)