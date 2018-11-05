from . import fabric
from . import searcher

def add_todo(tlist, args):
    if len(args) == 1:
        print("Please provide at least one argument: content list-title[optional]  status[optional]")
        return tlist
    
    elif len(args) == 2:
        if len(tlist) == 0:
            tlist.append(fabric.TodoList("inbox"))
            tlist[0].add_todo(args[1])
        else:
            tlist[0].add_todo(args[1])
        tlist[0].view_list()
        return tlist
    
    elif len(args) == 3:
        index_list = searcher.find_list_index(args[2], tlist)
        if index_list >= 0:
            tlist[index_list].add_todo(args[1])
            tlist[index_list].view_list()
        else:
            newlist = fabric.TodoList(args[2])
            newlist.add_todo(args[1])
            tlist.append(newlist)
            newlist.view_list()
    
    elif len(args.add) == 4:
        index_list = searcher.find_list_index(args[2], tlist)
        if index_list >= 0:
            tlist[index_list].add_todo(args[1], args[3])
            tlist[index_list].view_list()
        else:
            newlist = fabric.TodoList(args[2])
            newlist.add_todo(args[1], args[3])
            tlist.append(newlist)
            newlist.view_list()
    
    else:
        print("Error: Too many Arguments (Tip: use quotes to surround todo content)")

    # print("Added todo + ", args[1])

def mark_todo(tlist, args):
    if len(args) == 1:
        if len(tlist) >= 0:
            tlist[0].index_view()
            index = int(input("Which list you want to mark: "))
        if index < len(tlist):
            tlist[0].status = input("What is your new status: ")
            return tlist
        else:
            print("No default list found")

def view_todo(tlist, args):
    if len(args) == 1:
        args.append('index')
    index_list = searcher.find_list_index(args[1], tlist)

    if index_list >= 0:
        tlist[index_list].view_list()
    else:
        print("List with title " + args[1] + " could not be found!")

def view_task(tlist, args):
    if len(args) == 1:
        args.append('index')
    index_list = searcher.find_list_index(args[1], tlist)

    if index_list >= 0:
        tlist[index_list].view_list(only_done=True)
    else:
        print("List with title " + args[1] + " could not be found!")

def view_all(tlist, args):
    for tlist in tlist:
        print()
        tlist.view_list()