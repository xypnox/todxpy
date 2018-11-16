# -*- coding: utf-8 -*- 
from . import settings as stg

class Todo:
    """
    A class to represent a single todo
    A todo has content and status, default status is blank
    """
    def __init__(self, content='', tags=[], status=' '):
        self.__type__ = "Todo"
        self.content = content
        self.status = status
        self.tags = tags
        # self._index = 0
    
    def add_tag(self, tag):
        self.tags.append(tag)

    def __str__(self):
        output = '\033[31m' + stg.status_aliases(self.status) + '\033[0m  ' + self.content
        for tag in self.tags:
            output += stg.tag_decorator(tag)
        return output

    def without_tags(self):
        return '\033[31m' + stg.status_aliases(self.status) + '\033[0m  ' + self.content

    def change_status(self, status):
        self.status = status



def view_list(tlist, only_left=False):
    """
    View todos
    """
    # print()
    if only_left == False:
        for todo in tlist:
            print(todo)
    else:
        for todo in tlist:
            if todo.status not in stg.done_markers:
                print(todo)

def index_view(tlist, only_left=False):
    """
    View list's todos with indexes
    """
    if only_left == True:
        for i, todo in enumerate(tlist):
            if todo.status not in stg.done_markers:
                print(i, todo)
    else:
        for i, todo in enumerate(tlist):
            print(i, todo)

def todo_view(tlist, index):
    """
    View a specific todo of given index
    """
    try:
        print(tlist[index])
    except IndexError:
        print("ERROR: The given index doesn't exist")

# def tag_view(tlist):
#     """
#     View only the title and tags of the list
#     """
#     if len() != 0:
#         print("Tags :", str(self.tags).strip('[]'))
#     print()

def add_todo(tlist, content, status=" ", tags=[]):
    tlist.append(Todo(content, status=status, tags=tags))

def delete_todo(tlist, index):
    try:
        tlist.pop(index)
    except IndexError:
        print("ERROR: The given index doesn't exist")

def check_modifier(arg):
    if arg[0] in stg.modifiers:
        return True
    return False