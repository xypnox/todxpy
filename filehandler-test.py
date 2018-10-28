import json
import fabric
import os
from collections import namedtuple

def jdefault(o):
    return o.__dict__

# def object_decoder(obj):
#     if '__type__' in obj and obj['__type__'] == 'TodoList':
#         objT = fabric.TodoList(obj['title'], obj['tags'])
#         for todo in obj['inventory']:
#             objT.add_todo(todo['content'], todo['status'])
#         return objT
#     return obj
# # x = json2obj(data)

def list_decoder(objs):
    todolists = []
    for obj in objs:
        # print(obj)
        if '__type__' in obj and obj['__type__'] == 'TodoList':
            objT = fabric.TodoList(obj['title'], obj['tags'])
            for todo in obj['inventory']:
                objT.add_todo(todo['content'], todo['status'])
        else:
            objT = obj
        todolists.append(objT)
    return todolists

todolist = fabric.TodoList("Science Stuff", ['science', 'tech'])
todolist.add_todo("To make a reactor")
todolist.add_todo("Start a reactor")
todolist.add_todo("Workk on a reactor", "✗")
todolist.add_todo("Research a reactor", "✓")

todolists = [todolist, todolist, todolist]

jdump = json.dumps(todolists, default=jdefault)

# print(jdump)

with open("data.json", "w") as data_file:
    data_file.write(jdump)

with open("data.json") as data_file:
    read_data = data_file.read()
    # x = json.loads(read_data)
    y = list_decoder(json.loads(read_data))
    print(type(y[0]))
    y[0].view_list()