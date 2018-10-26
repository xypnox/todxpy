from yesnoquery import query_yes_no as qyn
import fabric
import argparse
import os

def main():
    todol = fabric.TodoList(input("Enter title : "), input("Enter tags : ").split())
    todol.view_list()
    todol.add_todo(input("Add todo content"))
    todol.add_todo(input("Add todo content"))
    todol.add_todo(input("Add todo content"))
    todol.view_list()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A CLI ToDo App')
    parser.add_argument('--add',
                        help='add a todo')
    parser.add_argument('--view',
                        default='inbox',
                        help='view the passed list by default views inbox')
    parser.add_argument('--all',
                        action='store_true',
                        help='view all the files')
    args = parser.parse_args()
    print(args)
    if args.add != None:
        print("Added todo + ", args.add)
    main()