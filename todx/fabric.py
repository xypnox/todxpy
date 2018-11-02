# -*- coding: utf-8 -*- 
from todx import settings as stg

class Todo:
    """
    A class to represent a single todo
    A todo has content and status, default status is blank
    """
    def __init__(self, content='', status=' '):
        self.__type__ = "Todo"
        self.content = content
        self.status = status
        # self._index = 0
    
    def __str__(self):
        return '[' + stg.status_aliases(self.status) + '] ' + self.content


class TodoList():
    """
    A class to represent a List of todos.
    The main list is inventory, and the list has a title and tags
    """

    def __init__(self, title, tags=[]):
        """
        This function creates and initialises empty TodoList with title and tags
        """
        self.__type__ = "TodoList" # useful for json serialization
        self.title = title
        self.tags = tags
        self.inventory = [] # list of objects of class Todo 

    def add_tag(self, tag):
        self.tags.append(tag)

    def change_title(self, title):
        self.title = title

    def view_list(self, only_done=False):
        """
        View list's title tags and todos
        """
        print(self.title)
        if len(self.tags) != 0:
            print("Tags :", str(self.tags).strip('[]'))
        print()
        if only_done == False:
            for todo in self.inventory:
                print(todo)
        else:
            for todo in self.inventory:
                if todo.status not in stg.done_markers:
                    print(todo)

    def index_view(self, only_done=False):
        """
        View list's todos with indexes
        """
        print(self.title)
        if len(self.tags) != 0:
            print("Tags :", str(self.tags).strip('[]'))
        print()
        if only_done == True:
            for i, todo in enumerate(self.inventory):
                if todo.status in stg.done_markers:
                    print(i + " ", todo)
        else:
            for i, todo in enumerate(self.inventory):
                print(i, " ", todo)

    def todo_view(self, index):
        """
        View a specific todo of given index
        """
        try:
            print(self.inventory[index])
        except IndexError:
            print("ERROR: The given index doesn't exist")

    def tag_view(self):
        """
        View only the title and tags of the list
        """
        print(self.title)
        if len(self.tags) != 0:
            print("Tags :", str(self.tags).strip('[]'))
        print()

    def add_todo(self, content, status=" "):
        self.inventory.append(Todo(content, status))
    
    def delete_todo(self, index):
        try:
            self.inventory.pop(index)
        except IndexError:
            print("ERROR: The given index doesn't exist")

    def change_status(self, index, status):
        try:
            self.inventory[index].status = status
        except IndexError:
            print("ERROR: The given index doesn't exist")
