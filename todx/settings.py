# -*- coding: utf-8 -*- 
status_aliases_dict = {
    'v': '🗹',
    'x': '🗷',
    ' ': '☐',
    'o': '🞆',
    '.': '⦿',
    'h': '⏺'
}

done_markers = ['v', '☑', 'x', '☒']

tag_marker = ''

version = '0.1.3'

modifiers = ['+', '#']

def status_aliases(status):
    if status in status_aliases_dict:
        return status_aliases_dict[status]
    return status

def tag_decorator(tag):
    return ' \033[94m\033[104;30m+' + tag + ' \033[0m '