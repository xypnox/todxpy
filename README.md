# todxpy
Python version of TodX

Probably I should add more readme stuff

To install the program run `pip install todx`


## Commands

Currently the supported commands are:

### `--add` or `-a`

Use this command to add a new todo

You have to pass the contents of the todo surrounded by quotes. You can also pass a list title and if no list is present with passed titles the program will create a new list for you. You can also pass a status after specifying the list.

If you don't specify the list, the first list i.e. Inbox will be used.

Format: `todx --add [content] [list](optional) [status](optional)`

### `--view` or `t`

Format: `todx --view [list title](optional, defaults to inbox)`

### `--task` or `-t`

Format: `todx --task [list title](optional, defaults to inbox)`

### `--all`

Format: `todx --all`


### Helptext
```
A CLI ToDo App

optional arguments:
  -h, --help            show this help message and exit
  -a [ADD [ADD ...]], --add [ADD [ADD ...]]
                        add a todo
  -m [MARK [MARK ...]], --mark [MARK [MARK ...]]
                        Mark a todo
  -v [VIEW], --view [VIEW]
                        view the passed list, by default views inbox
  -t [TASK], --task [TASK]
                        view the passed list left todos, by default views
                        inbox
  --all                 view all the files
  --version             show program's version number and exit
```