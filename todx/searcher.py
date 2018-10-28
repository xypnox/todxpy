# from . import fabric
from fuzzywuzzy import fuzz


def find_list_index(list_title, todolists):
    for i, tlist in enumerate(todolists):
        if fuzz.partial_ratio(list_title, tlist.title) > 80:
            return i
    return -1