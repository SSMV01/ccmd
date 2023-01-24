import sys
import logging
import os
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

username = os.environ.get("LOGNAME")

def set_target_file():
    if len(sys.argv) == 3:
        cmds_file_location = sys.argv[-1]
        if cmds_file_location == 'default':
            cmds_file_location = f'/home/{username}/ccmd/bin/cmds.csv'

        try:
            with open(f'/home/{username}/ccmd/bin/cmds_target.txt', 'w') as target_file:
                target_file.write(cmds_file_location)
            logging.info("Target File Saved.")
            sys.exit(0)

        except PermissionError:
            logging.error("Premission denied! Try running the command with 'sudo'.")
            sys.exit(2)
    else:
        logging.error("File path not specified OR More than one options used.")
        logging.info("Please use only one option.")
        sys.exit(2)