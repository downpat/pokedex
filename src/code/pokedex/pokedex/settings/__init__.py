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

REDIS_PASS = "gottaC47TCHem477"


CELERY_BROKER = f'redis://:{REDIS_PASS}@192.168.165.26:6379/0'
