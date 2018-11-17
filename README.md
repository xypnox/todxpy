# todxpy
![Travis (.org)](https://img.shields.io/travis/xypnox/todxpy.svg?style=flat-square)

A simple and easy to use yet configurable todo app.

## Installation

To install the program run

```bash
$ pip install todx
```

If you are using Ubuntu run this instead:

```
$ pip3 install todx
```



To check whether the installation was successful run:

```bash
$ todx -v
```

This should output something like `TodX vX.X.X`  depending on your version number

## Usage

You can add todos using the `todx add` command:

```bash
$ todx add Make me a sandwich
```

You can mark a todo using `todx mark` command:

```bash
$ todx mark
0 ☐  Make a great website 

Which todo you want to mark: 0
What is your new status: v
```

To see todos you just need to run the `todx` command:

```
$ todx
☐  Make me a sandwich
```

To view todos that you that you have already marked also, run `todx view`.

There are only few characters that are recognized as a completed todo, they given below:

| Character | Representation |
| :-------: | :------------: |
|     v     |       ☑        |
|     x     |       ☒        |
| \<space\> |       ☐        |

 

You can remove a todo using `todx del` command (It works similar to `todx mark`).

You can use tags for todos, Just add a `+` before your work to add it to a todo.

```bash
$ todx add Make a python script to fetch data +project
```

To view todos of current tags use `todx +tagname`

A detailed blogpost covering the use is at : https://xypnox.github.io/blag/posts/todx-the-todo-manager/