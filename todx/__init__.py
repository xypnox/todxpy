#!/usr/bin/env python3
from . import main
from . import settings as stg

name = 'todx'
__version__ = stg.version


if __name__ == '__main__':
    main.main_command()
