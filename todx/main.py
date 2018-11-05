#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# import os
import argparse
import appdirs
import sys

from . import filehandler
from . import parse_functions as pf
# from yesnoquery import query_yes_no as qyn

def main_command():
    # Load datafile and parse arguments
    app_data_file = appdirs.user_data_dir('todx') + '/data.json'

    tlist = filehandler.load_file(app_data_file)
    # print(tlist)

    args = sys.argv[1:]
    print('Arguments passed are : ', args)

    if len(args) == 0:
        args.append('task')
        pf.parse_task(tlist, args)
    
    elif args[0] == 'add':
        pf.parse_add(tlist, args)

    elif args[0] == 'mark':
        pf.parse_mark(tlist, args)

    elif args[0] == 'view':
        pf.parse_view(tlist, args)

    elif args[0] == 'task':
        pf.parse_task(tlist, args)
    # Final cleanup and close
    filehandler.save_file(app_data_file, tlist)
