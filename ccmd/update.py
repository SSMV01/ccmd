import os
import sys
from utils import exception_handler


USERNAME = os.environ.get('LOGNAME')

def get_update():
    try:
        os.chdir(f'/home/{USERNAME}/.ccmd')
        os.system(f'{sys.executable} get_update.py')
        sys.exit(0)

    except FileNotFoundError:
        exception_handler.file_not_found('get_ccmd.py')

    except KeyboardInterrupt:
        exception_handler.keyboard_interrupt()
