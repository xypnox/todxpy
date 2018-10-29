# -*- coding: utf-8 -*- 
from fuzzywuzzy import fuzz
# from todx import fabric


def find_list_index(list_title, todolists):
    for i, tlist in enumerate(todolists):
        if fuzz.partial_ratio(list_title, tlist.title) > 80:
            return i
    return -1