import sys
import logging
import os
from pathlib import Path
from utils import exception_handler


# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

username = os.environ.get("LOGNAME")

def set_csv_file(csv_file_location):
    if csv_file_location == 'default':
        csv_file_location = f'/home/{username}/.ccmd/bin/cmds.csv'

    csv_file_location = os.path.abspath(csv_file_location)

    if Path(csv_file_location).is_file():
        with open(f'/home/{username}/.ccmd/bin/cmds_target.txt', 'w', encoding='utf-8') as target_file:
            target_file.write(csv_file_location)
        logging.info("csv file set.")
        sys.exit(0)
    else:
        exception_handler.file_not_found(csv_file_location)
