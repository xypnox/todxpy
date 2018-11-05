# import json
from todx import fabric
# import os
# from collections import namedtuple
from todx import filehandler



todolist = []
fabric.add_todo(todolist, "To make a reactor")
fabric.add_todo(todolist, "Start a reactor")
fabric.add_todo(todolist, "Workk on a reactor", "✗")
fabric.add_todo(todolist, "Research a reactor", "✓", ['science', 'todx'])

filehandler.save_file("data.json", todolist)
# print(jdump)

# with open("data.json", "w") as data_file:
#     data_file.write(jdump)

tlist2 = filehandler.load_file("data.json")

for todo in tlist2:
    print(todo)