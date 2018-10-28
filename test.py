import fabric as fb

T1 = fb.Todo("Idiot am I", "o")

print(T1.content)
print(T1.status)

stk = fb.TodoList("Man at Arms", ["cool", "Awesome"])

stk.add_todo("Bang", "0")
stk.add_todo("Awesome stuff needs to be done")

stk.view_list()

