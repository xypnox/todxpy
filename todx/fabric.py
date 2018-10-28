from . import settings

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
        return '[' + settings.status_aliases(self.status) + '] ' + self.content


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

    def view_list(self):
        """
        View list's title tags and todos
        """
        print(self.title)
        if len(self.tags) != 0:
            print("Tags :", str(self.tags).strip('[]'))
        print()
        for item in self.inventory:
            print(item)

    def index_view(self):
        """
        View list's title tags and todos with indexes
        """
        print(self.title)
        if len(self.tags) != 0:
            print("Tags :", str(self.tags).strip('[]'))
        print()
        for i in range(len(self.inventory)):
            print(i + " ", self.inventory[i])
    
    def todo_view(self, index):
        """
        View a specific todo of given index
        """
        try:
            print(self.inventory[index])
        except IndexError:
            print("ERROR: The given index doesn't exist")

    def tag_index_view(self):
        """
        View only the index and tags of the list
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
