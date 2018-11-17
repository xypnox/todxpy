from todx import __version__
from todx import fabric

def test_version():
    assert __version__ == '0.1.3'

def test_todo():
    todo = fabric.Todo('I am Awesome', ['science'], 'x')
    print(todo)
    assert 1