# -*- coding: utf-8 -*- 
from fuzzywuzzy import process
# from todx import fabric


def find_index_tag(tag, tlist):
    """
    Returns a list with first element as tag and rest indexes of todos with that tag
    """
    index_list = []
    similar_tags = []
    for i, todo in enumerate(tlist):
        similar_tags = process.extract(tag, todo.tags)
        if len(similar_tags) > 0:
            if len(index_list) == 0:
                index_list.append(similar_tags[0][0])
            if similar_tags[0][1] > 70:
                index_list.append(i)
    return index_list