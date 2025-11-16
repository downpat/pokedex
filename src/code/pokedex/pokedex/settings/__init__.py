from sys import exit

from .main import *

try:
    from .prod import *
except ModuleNotFoundError as mnfe:
    try:
        from .local import *
    except ModuleNotFoundError as mnfe:
        print('No local or production settings found. Exiting...')
        exit(1)
