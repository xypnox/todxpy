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

    args = sys.argv[1:]
    print('Arguments passed are : ', args)

    if len(args) == 0:
        args.append('task')
        pf.view_task(tlist, args)
    
    elif args[0] == 'add':
        tlist = pf.add_todo(tlist, args)

    elif args[0] == 'mark':
        tlist = pf.mark_todo(tlist, args)

    elif args[0] == 'view':
        pf.view_todo(tlist, args)

    elif args[0] == 'task':
        pf.view_task(tlist, args)
    
    elif args[0] == 'all':
        pf.view_all(tlist, args)
    
    # Final cleanup and close
    filehandler.save_file(app_data_file, tlist)
