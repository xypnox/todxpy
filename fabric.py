class Todo:
    def __init__(self, content="", status=" "):
        self.content = content
        self.status = status

class Stak:
    def __init__(self, title, tags=[]):
        self.inventory = []
        self.title = title
        self.tags = tags

    def add_tag(self, tag):
        self.tags.append(tag)

    def change_title(self, title):
        self.title = title

    def add_todo(self, content, status=" "):
        self.inventory.push(Todo(content, status))

    def view_stak(self):
        for item in self.inventory:
            print(self.title)
            if len(self.tags) != 0:
                print("Tags :", end=" ")
                for tag in self.tags:
                    print(tag, end=", ")
                print()
            print(" ["+item.status+"] : " + item.content)
