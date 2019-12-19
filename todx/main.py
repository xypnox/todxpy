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

    twrap = filehandler.load_file(app_data_file)

    args = sys.argv[1:]
    #print('Arguments passed are : ', args)
    if len(args) == 0:
        args.append('task')
        pf.parse_task(twrap, args)
    
    elif args[0] == 'add' or args[0] == '-a':
        pf.parse_add(twrap, args)

    elif args[0] == 'mark' or args[0] == '-m':
        pf.parse_mark(twrap, args)

    elif args[0] == 'view':
        pf.parse_view(twrap, args)

    elif args[0] == 'task':
        pf.parse_task(twrap, args)

    elif args[0] == 'edit':
        pf.parse_edit(twrap, args)

    elif args[0] == 'tags':
        pf.parse_tags(twrap, args)
    
    elif args[0] == 'del':
        pf.parse_del(twrap, args)

    elif args[0] == '--version' or args[0] == '-v':
        print('TodX v' + stg.version)

    elif args[0] == '--help' or args[0] == '-h':
        file_reader=open('todx/man.txt','r')
        print(file_reader.read())


    elif args[0][0] == '+':
        args.insert(0, 'task')
        pf.parse_task(twrap, args)

    else:
        print("Unknown commands: ", args)

    # Final cleanup and close
    filehandler.save_file(app_data_file, twrap)
