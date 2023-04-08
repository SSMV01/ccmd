import os
import logging

USERNAME = os.environ.get('LOGNAME')


def uninstall():
    try:
        os.chdir(f'/home/{USERNAME}/.ccmd')
        os.system('bash uninstall.sh')
        exit(0)

    except FileExistsError:
        logging.error(f".ccmd directory not found at /home/{USERNAME}/")
        exit(2)
