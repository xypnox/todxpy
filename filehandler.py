import json
import fabric
import os

def jdefault(o):
    return o.__dict__

todolist = fabric.TodoList("Science Stuff", ['science', 'tech'])
todolist.add_todo("To make a reactor")
todolist.add_todo("Start a reactor")
todolist.add_todo("Workk on a reactor", "✗")
todolist.add_todo("Research a reactor", "✓")

jdump = json.dumps(todolist, default=jdefault)

print(jdump)
