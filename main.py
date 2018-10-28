from yesnoquery import query_yes_no as qyn
import fabric
import argparse
import os
import appdirs
import filehandler
import searcher

def main():
    todol = fabric.TodoList(input("Enter title : "), input("Enter tags : ").split())
    todol.view_list()
    todol.add_todo(input("Add todo content"))
    todol.add_todo(input("Add todo content"))
    todol.add_todo(input("Add todo content"))
    todol.view_list()


if __name__ == '__main__':
    # Load datafile and parse arguments
    app_data_file = appdirs.user_data_dir('todx') + '/data.json'

    todolists = filehandler.load_file(app_data_file)

    parser = argparse.ArgumentParser(description='A CLI ToDo App')
    parser.add_argument('-a', '--add', nargs='*',
                        help='add a todo')
    parser.add_argument('--view',
                        default='inbox',
                        help='view the passed list by default views inbox')
    parser.add_argument('--all',
                        action='store_true',
                        help='view all the files')
    args = parser.parse_args()
    # print(args)


    if args.add != None:
        
        if len(args.add) == 1:
            if len(todolists) == 0:
                todolists.append(fabric.TodoList("inbox"))
                todolists[0].add_todo(args.add[0])
            else:
                todolists[0].add_todo(args.add[0])
            todolists[0].view_list()
        # print("Added todo + ", args.add[0])
        
        # elif len(args.add) == 2:
        #     if 


    # Final cleanup and close
    filehandler.save_file(app_data_file, todolists)
    # main()