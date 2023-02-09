import sys
import logging
import os
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

username = os.environ.get("LOGNAME")

def set_target_file(cmds_file):
    if len(sys.argv) == 3:
        cmds_file_location = cmds_file
        if cmds_file_location == 'default':
            cmds_file_location = f'/home/{username}/ccmd/bin/cmds.csv'

        try:
            with open(f'/home/{username}/ccmd/bin/cmds_target.txt', 'w') as target_file:
                target_file.write(cmds_file_location)
            if cmds_file_location == "default":
                logging.info("Default Set.")
                sys.exit(0)
            logging.info("Target File Set.")
            sys.exit(0)

        except PermissionError:
            logging.error("Premission denied! Try running the command with 'sudo'.")
            sys.exit(2)