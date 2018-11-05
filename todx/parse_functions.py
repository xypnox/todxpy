from . import fabric
from . import searcher

def parse_modifier(newtodo, arg):
    if arg[0] == '+':
        newtodo.add_tag(arg[1:])
    # elif arg[1] == '':


def parse_add(tlist, args):
    if len(args) == 1:
        print("Please provide at least one argument: content list-title[optional]  status[optional]")
    
    elif len(args) == 2:
        fabric.add_todo(tlist, args[1])
        print("Added todo + ", args[1])
    
    else:
        newtodo = fabric.Todo()
        for arg in args[1:]:
            if fabric.check_modifier(arg) is False:
                newtodo.content += arg + ' '
            else:
                parse_modifier(newtodo, arg)
        tlist.append(newtodo)
        print('Added todo: ', newtodo)


def parse_mark(tlist, args):
    if len(args) == 1:
        if len(tlist) >= 0:
            tlist[0].index_view()
            index = int(input("Which list you want to mark: "))
        if index < len(tlist):
            tlist[0].status = input("What is your new status: ")
        else:
            print("No default list found")


def parse_view(tlist, args):
    if len(args) == 1:
        for todo in tlist:
            print(todo)
        return

    index_list = searcher.find_index_tag(args[1], tlist)
    if len(index_list) == 0:
        print("No todos with tag " + args[1] + " found!")
        return
    print('+', index_list[0])
    for index in index_list[1:]:
        print(tlist[index].without_tags())


def parse_task(tlist, args):
    fabric.view_list(tlist, only_left=True)