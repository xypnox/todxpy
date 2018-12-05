# -*- coding: utf-8 -*- 
import json
import os
import errno
from . import fabric
# from collections import namedtuple

def jdefault(o):
    return o.__dict__

def list_decoder(objs):
    """
    Function to parse the json list of dictionary into objects of TodoList.
    """
    # print(objs)
    twrap = fabric.TodoWrapper()
    twrap.createTime = objs['createTime']
    twrap.username = objs['username']
    twrap.cookie = objs['cookie']

    for obj in objs['tlist']:
        if '__type__' in obj and obj['__type__'] == 'Todo':
            objT = fabric.Todo(obj['content'], obj['tags'], obj['status'])
        else:
            objT = obj
        twrap.tlist.append(objT)
    return twrap

def load_file(filename):
    """
    Function to load datafiles, it returns a list of Todo
    """
    if not os.path.exists(os.path.dirname(filename)) and '/' in filename:
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
        return fabric.TodoWrapper()

    if os.path.isfile(filename):
        with open(filename, 'r+') as data_file:
            read_data = data_file.read()
            return list_decoder(json.loads(read_data))
    else:
        with open(filename, 'w') as data_file:
            return fabric.TodoWrapper()

def save_file(filename, data):
    """
    Function to save data <list of TodoList Objects> to a json file in json format 
    """
    with open(filename, 'w+') as data_file:
        jsondata = json.dumps(data, default=jdefault, indent=4)
        data_file.write(jsondata)
