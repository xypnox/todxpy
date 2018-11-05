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
    
    else:
        newtodo = fabric.Todo()
        for arg in args[1:]:
            if fabric.check_modifier(arg) is False:
                newtodo.content += arg + ' '
            else:
                parse_modifier(newtodo, arg)
        tlist.append(newtodo)
    print("Added todo + ", args[1])


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
        args.append('index')
    index_list = searcher.find_list_index(args[1], tlist)

    if index_list >= 0:
        tlist[index_list].view_list()
    else:
        print("List with title " + args[1] + " could not be found!")


def parse_task(tlist, args):
    fabric.view_list(tlist, only_left=True)