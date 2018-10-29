# import json
from . import fabric
# import os
# from collections import namedtuple
from . import filehandler



todolist = fabric.TodoList("Science Stuff", ['science', 'tech'])
todolist.add_todo("To make a reactor")
todolist.add_todo("Start a reactor")
todolist.add_todo("Workk on a reactor", "✗")
todolist.add_todo("Research a reactor", "✓")

todolists = [todolist, todolist, todolist]

filehandler.save_file("data.json", todolists)
# print(jdump)

# with open("data.json", "w") as data_file:
#     data_file.write(jdump)

todolists2 = filehandler.load_file("data.json")

for tlist in todolists2:
    tlist.view_list()