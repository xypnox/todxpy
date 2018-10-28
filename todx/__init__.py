name='todx'
name = 'todx'

#!/usr/bin/env python3
# import os
import argparse
import appdirs
from . import settings
from . import fabric
from . import filehandler
from . import searcher
# from yesnoquery import query_yes_no as qyn

def main_command():
    # Load datafile and parse arguments
    app_data_file = appdirs.user_data_dir('todx') + '/data.json'

    todolists = filehandler.load_file(app_data_file)

    parser = argparse.ArgumentParser(description='A CLI ToDo App')
    parser.add_argument('-a', '--add',
                        nargs='*',
                        help='add a todo')
    parser.add_argument('-v', '--view',
                        default=None,
                        const='inbox',
                        nargs='?',
                        help='view the passed list by default views inbox')
    parser.add_argument('--all',
                        action='store_true',
                        help='view all the files')
    args = parser.parse_args()
    # print(args)


    if args.add != None:
        if len(args.add) == 0:
            print("Please provide at least one argument: content list-title[optional]  status[optional]")
        elif len(args.add) == 1:
            if len(todolists) == 0:
                todolists.append(fabric.TodoList("inbox"))
                todolists[0].add_todo(args.add[0])
            else:
                todolists[0].add_todo(args.add[0])
            todolists[0].view_list()
        # print("Added todo + ", args.add[0])
        
        elif len(args.add) == 2:
            index_list = searcher.find_list_index(args.add[1], todolists)
            if index_list >= 0:
                todolists[index_list].add_todo(args.add[0])
                todolists[index_list].view_list()
            else:
                newlist = fabric.TodoList(args.add[1])
                newlist.add_todo(args.add[0])
                todolists.append(newlist)
                newlist.view_list()
        
        elif len(args.add) == 3:
            index_list = searcher.find_list_index(args.add[1], todolists)
            if index_list >= 0:
                todolists[index_list].add_todo(args.add[0], args.add[2])
                todolists[index_list].view_list()
            else:
                newlist = fabric.TodoList(args.add[1])
                newlist.add_todo(args.add[0], args.add[2])
                todolists.append(newlist)
                newlist.view_list()
        
        else:
            print("Error: Too many Arguments (Tip: use quotes to surround todo content)")

    if args.view is not None:
        index_list = searcher.find_list_index(args.view, todolists)

        if index_list >= 0:
            todolists[index_list].view_list()
        else:
            print("List with title " + args.view + " could not be found!")
    
    if args.all is not False:
        for tlist in todolists:
            print()
            tlist.view_list()
    # Final cleanup and close
    filehandler.save_file(app_data_file, todolists)

if __name__ == '__main__':
    main_command()
