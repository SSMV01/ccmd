import os
import sys
import logging


USERNAME = os.environ.get('LOGNAME')

def get_update():
    try:
        os.chdir(f'/home/{USERNAME}/.ccmd')
        os.system(f'{sys.executable} get_update.py')
        sys.exit(0)
    
    except FileNotFoundError:
        logging.error("get_ccmd.py not found!")
    
    except KeyboardInterrupt:
        print()
        logging.info("Exiting...")
        sys.exit(1)
