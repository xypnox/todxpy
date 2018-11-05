# -*- coding: utf-8 -*- 
from fuzzywuzzy import process
# from todx import fabric


def find_index_tag(tag, tlist):
    indices = []
    for i, todo in enumerate(tlist):
        similar_tags = process.extract(tag, todo.tags)
        print(similar_tags)
        if len(similar_tags) > 0:
            if similar_tags[0][1] > 70:
                indices.append(i)
    return indices