# -*- coding: utf-8 -*- 
from . import settings as stg
import time

class Todo:
    """
    A class to represent a single todo
    A todo has content and status, default status is blank
    """
    def __init__(self, content='', tags=None, status=' '):
        if tags is None:
            tags = []
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
    
    def __eq__(self, other):
        if self.content == other.content and self.status == other.status and self.tags == other.tags:
            return True
        return False

    def without_tags(self):
        return '\033[31m' + stg.status_aliases(self.status) + '\033[0m  ' + self.content

    def change_status(self, status):
        self.status = status


class TodoWrapper:
    """
    A class that wraps the todos as a list and serves to have all the metadata about the todos
    """
    def __init__(self, createTime=time.gmtime()):
        self.createTime = createTime
        self.username = ''
        self.cookie = ''
        self.tlist = []

    def __len__(self):
        return len(self.tlist)

def view_list(twrap, only_left=False):
    """
    View todos
    """
    # print()
    if only_left is False:
        for todo in twrap.tlist:
            print(todo)
    else:
        for todo in twrap.tlist:
            if todo.status not in stg.done_markers:
                print(todo)

def index_view(twrap, only_left=False):
    """
    View list's todos with indexes
    """
    if only_left is True:
        for i, todo in enumerate(twrap.tlist):
            if todo.status not in stg.done_markers:
                print(i, todo)
    else:
        for i, todo in enumerate(twrap.tlist):
            print(i, todo)

def todo_view(twrap, index):
    """
    View a specific todo of given index
    """
    try:
        print(twrap.tlist[index])
    except IndexError:
        print("ERROR: The given index doesn't exist")

# def tag_view(tlist):
#     """
#     View only the title and tags of the list
#     """
#     if len() != 0:
#         print("Tags :", str(self.tags).strip('[]'))
#     print()

def add_todo(twrap, content, status=" ", tags=None):
    if tags is None:
        tags = []
    twrap.tlist.append(Todo(content, status=status, tags=tags))

def delete_todo(twrap, index):
    try:
        twrap.tlist.pop(index)
    except IndexError:
        print("ERROR: The given index doesn't exist")

def check_modifier(arg):
    if arg[0] in stg.modifiers:
        return True
    return False