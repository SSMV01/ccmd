import sys
import logging
from os import getlogin
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)


def set_target_file():
    if len(sys.argv) == 3:
        cmds_file_location = sys.argv[-1]
        try:
            with open(f'/home/{getlogin()}/customcmd/bin/cmds_target.txt', 'w') as target_file:
                target_file.write(cmds_file_location)
            logging.info("Target File Saved.")
        except PermissionError:
            logging.error("Premission denied! Try running the command with 'sudo'.")
    else:
        logging.error("File path not specified OR More than one options used.")
        logging.info("Please use only one option.")
        sys.exit(2)