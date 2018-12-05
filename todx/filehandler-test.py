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
fabric.add_todo(twrap.tlist, "To make a reactor")
fabric.add_todo(twrap.tlist, "Start a reactor")
fabric.add_todo(twrap.tlist, "Workk on a reactor", "✗")
fabric.add_todo(twrap.tlist, "Research a reactor", "✓", ['science', 'todx'])

filehandler.save_file("data.json", twrap)
# print(jdump)

# with open("data.json", "w") as data_file:
#     data_file.write(jdump)

twrap2 = filehandler.load_file("data.json")

print(twrap.username)
print(twrap.cookie)
print(twrap.createTime)
print(time.gmtime()==twrap.createTime)
for todo in twrap2.tlist:
    print(todo)