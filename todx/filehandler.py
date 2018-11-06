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
    tlist = []
    for obj in objs:
        # print(obj)
        if '__type__' in obj and obj['__type__'] == 'Todo':
            objT = fabric.Todo(obj['content'], obj['tags'], obj['status'])
        else:
            objT = obj
        tlist.append(objT)
    return tlist

def load_file(filename):
    """
    Function to load datafiles, it returns a list of Todo
    """
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
        return []

    if os.path.isfile(filename):
        with open(filename, 'r+') as data_file:
            read_data = data_file.read()
            return list_decoder(json.loads(read_data))
    else:
        with open(filename, 'w') as data_file:
            return []

def save_file(filename, data):
    """
    Function to save data <list of TodoList Objects> to a json file in json format 
    """
    with open(filename, 'w+') as data_file:
        jsondata = json.dumps(data, default=jdefault, indent=4)
        data_file.write(jsondata)

"""
I understand that my json data encoder and decoder are absolute crap However they work and thats what is great. I have borrowed code from about 4 stackoverflow answers and used some trial and error to get to this stage. I would love to refactor it, but I would love to do a lot of other things, so this remains as it is. Do not modify this unless you are brave enough (and crazy enough).
"""