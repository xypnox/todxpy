# -*- coding: utf-8 -*- 
status_aliases_dict = {
    'v': '☑',
    'x': '☒',
    ' ': '☐'
}

done_markers = ['v', '☑', 'x', '☒', 'o']

version = '0.1.0'

modifiers = ['+', '#']

def status_aliases(status):
    if status in status_aliases_dict:
        return status_aliases_dict[status]
    return status
