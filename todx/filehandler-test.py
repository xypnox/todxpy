# import json
from todx import fabric
# import os
# from collections import namedtuple
from todx import filehandler
import time


twrap = fabric.TodoWrapper()
twrap.createTime = time.gmtime()
twrap.username = 'xypnox'
twrap.cookie = 'abcdABCD'
fabric.add_todo(twrap, "To make a reactor")
fabric.add_todo(twrap, "Start a reactor")
fabric.add_todo(twrap, "Workk on a reactor", "✗")
fabric.add_todo(twrap, "Research a reactor", "✓", ['science', 'todx'])

filehandler.save_file("data.json", twrap)
# print(jdump)

# with open("data.json", "w") as data_file:
#     data_file.write(jdump)

twrap2 = filehandler.load_file("data.json")

print(twrap.username)
print(twrap.cookie)
print(twrap.createTime)
print(time.gmtime()==twrap.createTime)
print(len(twrap))
for todo in twrap2.tlist:
    print(todo)