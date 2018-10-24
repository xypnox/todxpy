from yesnoquery import query_yes_no as qyn
import fabric

def main():
    todol = fabric.TodoList(input("Enter title : "), input("Enter tags : ").split())
    todol.view_list()
    todol.add_todo(input("Add todo content"))
    todol.add_todo(input("Add todo content"))
    todol.add_todo(input("Add todo content"))
    todol.view_list()

if __name__ == '__main__':
    main()