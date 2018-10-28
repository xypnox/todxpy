import json
from . import fabric
import os
import errno
# from collections import namedtuple

def jdefault(o):
    return o.__dict__

def list_decoder(objs):
    """
    Function to parse the json list of dictionary into objects of TodoList.
    """
    todolists = []
    for obj in objs:
        # print(obj)
        if '__type__' in obj and obj['__type__'] == 'TodoList':
            objT = fabric.TodoList(obj['title'], obj['tags'])
            for todo in obj['inventory']:
                objT.add_todo(todo['content'], todo['status'])
        else:
            objT = obj
        todolists.append(objT)
    return todolists

def load_file(filename):
    """
    Function to load datafiles, it returns a list of TodoList objects
    """
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
        return []

    with open(filename) as data_file:
        read_data = data_file.read()
        return list_decoder(json.loads(read_data))

def save_file(filename, data):
    """
    Function to save data <list of TodoList Objects> to a json file in json format 
    """
    with open(filename, "w+") as data_file:
        jsondata = json.dumps(data, default=jdefault, indent=4)
        data_file.write(jsondata)

"""
I understand that my json data encoder and decoder are absolute crap However they work and thats what is great. I have borrowed code from about 4 stackoverflow answers and used some trial and error to get to this stage. I would love to refactor it, but I would love to do a lot of other things, so this remains as it is. Do not modify this unless you are brave enough (and crazy enough).
"""