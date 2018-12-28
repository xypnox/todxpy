from . import fabric
from . import searcher
import readline
import cutie
from . import settings as stg
from . yesnoquery import query_yes_no

def parse_modifier(newtodo, arg):
    """
    Parse a sepecial modifier argument
    Current mod:
        +   add
    """
    if arg[0] == '+':
        newtodo.add_tag(arg[1:])
    # elif arg[1] == '':


def parse_add(twrap, args):
    """
    Parse the add command
     - If no arguments prints help for add
     - If 1 argument creates new todo with argument as content
     - If more arguments joins arguments into content and seperates modifiers
    """

    if len(args) == 1:
        print("Please provide at least one argument: content tags[optional]  status[optional]")
    
    elif len(args) == 2:
        fabric.add_todo(twrap, args[1])
        print("Added todo + ", args[1])
    
    else:
        newtodo = fabric.Todo()
        for arg in args[1:]:
            if fabric.check_modifier(arg) is False:
                newtodo.content += arg + ' '
            else:
                if len(arg) == 1:
                    newtodo.content += arg + ' '
                else:
                    parse_modifier(newtodo, arg)
        twrap.tlist.append(newtodo)
        print('Added todo: ', newtodo)


def parse_mark(twrap, args):
    """
    Parse mark command
    """
    if len(args) == 1:
        if len(twrap) > 0:
            fabric.index_view(twrap)
            print()
            print("Which todo do you want to mark: ")
            selection = twrap[cutie.select(twrap)]
            index = twrap.index(selection)
            
            #index = int(input("Which todo you want to mark: "))
            if index < len(twrap):
                stats = ['x', 'v', ' ']
                print("What is your new status: ")
                twrap[index].status = stats[cutie.select(stats)]
                #twrap[index].status = input("What is your new status: ")
            else:
                print('Too large an Index, You have.')
        else:
            print("No todo list found")


def parse_view(twrap, args):
    """
    Parse view command
     - If no other arguments are passed view every todo
     - if an argument is passed view todos tagged as the argument
    """
    if len(args) == 1:
        fabric.view_list(twrap)
        return

    if args[1][0] == '+':
        args[1] = args[1][1:]

    index_list = searcher.find_index_tag(args[1], twrap.tlist)

    if len(index_list) == 0:
        print("No todos with tag " + stg.tag_decorator(args[1]) + " found!")
        return
    
    print(stg.tag_decorator(args[1]))
    for index in index_list[1:]:
        print(twrap.tlist[index].without_tags())


def parse_task(twrap, args):
    """
    Parse task command
     - If no other arguments are passed view every undone todo
     - if an argument is passed view undone todos tagged as the argument
    """
    if len(args) == 1:
        fabric.view_list(twrap, only_left=True)
        return

    if args[1][0] == '+':
        args[1] = args[1][1:]

    index_list = searcher.find_index_tag(args[1], twrap.tlist)
    
    if len(index_list) == 0:
        print("No todos with tag " + stg.tag_decorator(args[1]) + " found!")
        return
    
    print(stg.tag_decorator(args[1]))
    for index in index_list[1:]:
        if twrap.tlist[index].status not in stg.done_markers:
            print(twrap.tlist[index].without_tags())


def parse_del(twrap, args):
    """
    Parse del command
    """
    if len(args) == 1:
        if len(twrap) > 0:
            fabric.index_view(twrap)
            print()
            print("Which todo do you want to delete: ")
            selection = twrap[cutie.select(twrap)]
            index = twrap.index(selection)
            #index = int(input("Which todo you want to delete: "))
            if index < len(twrap):
                if query_yes_no('Are you sure buddy?') is True:
                    del twrap[index]
            else:
                print('Too large an Index, You have.')
        else:
            print("No todo list found")

def rlinput(prompt, prefill = ''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)
   finally:
      readline.set_startup_hook()

def parse_edit(twrap, args):
    """
    Parse edit command
    """
    if len(args) == 1:
        if len(twrap) > 0:
            fabric.index_view(twrap)
            print()
            index = int(input("Which todo you want to edit: "))
            if index < len(twrap):
                sub_str = rlinput("edit here : ",twrap.tlist[index].content)
                if len(sub_str) == 0 : 
                    print("todo item cannot be empty")
                else:
                    if query_yes_no('Are you sure buddy?') is True:
                        twrap.tlist[index].content = sub_str
            else:
                print('Too large an Index, You have.')
        else:
            print("No todo list found")

def parse_tags(twrap, args):
    """
    Parse tags command
    """
    if len(args) == 1:
        if len(twrap) > 0:
            fabric.index_view(twrap)
            print()
            index = int(input("Which todo tags do you want to edit: "))
            if index < len(twrap) and index > -1:
                cur_tags = [ i for i in twrap.tlist[index].tags ]
                print("current tags : ",' , '.join(i for i in twrap.tlist[index].tags))
                sub_str = input("do +[tag] to add , -[tag] to remove : ")
                sub_str = [i for i in sub_str.split()]
                for i in sub_str:
                    if i[0] == '+' and len(i) > 1:
                        twrap.tlist[index].tags.append(i[1:])
                    elif i[0] == '-' and i[1:] in cur_tags:
                        twrap.tlist[index].tags.remove(i[1:])        
            else:
                print('Invalid Index, You have.')
        else:
            print("No todo list found")


