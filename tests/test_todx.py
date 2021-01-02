from todx import __version__
from todx import fabric

def test_version():
    if __version__ != '0.1.3':
        raise AssertionError

def test_todo():
    todo = fabric.Todo('I am Awesome', ['science'], 'x')
    print(todo)
    assert 1