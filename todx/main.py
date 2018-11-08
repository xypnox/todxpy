#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# import os
import argparse
import appdirs
import sys

from . import filehandler
from . import parse_functions as pf
from . import settings as stg

def main_command():
    # Load datafile and parse arguments
    app_data_file = appdirs.user_data_dir('todx') + '/data.json'

    tlist = filehandler.load_file(app_data_file)

    args = sys.argv[1:]
    # print('Arguments passed are : ', args)

    if len(args) == 0:
        args.append('task')
        pf.parse_task(tlist, args)
    
    elif args[0] == 'add' or args[0] == '-a':
        pf.parse_add(tlist, args)

    elif args[0] == 'mark' or args[0] == '-m':
        pf.parse_mark(tlist, args)

    elif args[0] == 'view':
        pf.parse_view(tlist, args)

    elif args[0] == 'task':
        pf.parse_task(tlist, args)
    
    elif args[0] == 'del':
        pf.parse_del(tlist, args)

    elif args[0] == '--version' or args[0] == '-v':
        print('TodX v' + stg.version)

    elif args[0][0] == '+':
        args.insert(0, 'task')
        pf.parse_task(tlist, args)

    else:
        print("Unknown commands: ", args)

    # Final cleanup and close
    filehandler.save_file(app_data_file, tlist)
