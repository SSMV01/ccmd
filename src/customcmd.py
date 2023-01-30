#!/usr/bin/python3
import os
import sys
import logging
from libry import (create_command, set_target_file, run_command, help)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

version = 'ccmd 0.2.5-alpha'
username = os.environ.get("LOGNAME")

try:
    with open(f'/home/{username}/ccmd/bin/cmds_target.txt', 'r') as target_file:
        csv_file = target_file.read()
except FileNotFoundError:
    logging.error(f"Could not find 'cmds_target' at /home/{username}/customcmd/bin/cmds_target.")
    logging.info("Check if file has been deleted or moved or renamed.")
    sys.exit(2)


def main():
    if '-h' in sys.argv or '--help' in sys.argv:
        help()
    elif '-v' in sys.argv or '--version' in sys.argv:
        print(version)
        sys.exit(0)
    elif '--target' in sys.argv:
        set_target_file()

    if csv_file.isspace() or csv_file == '':
        logging.error("No file specified in 'cmds_target.txt'.")
        logging.info("Use '--target' to specify the location of the csv file.")
        sys.exit(2)
    elif '--opencsv' in sys.argv:
        os.system(f'xdg-open {csv_file}')
        sys.exit(0)
    elif '-new' in sys.argv:
        create_command(csv_file)
    else:
        run_command(csv_file)


if len(sys.argv) < 2:
    logging.error("No Input given.")
    logging.info("Type 'ccmd --help' for usage info.")
    sys.exit(2)
else:
    if __name__ == '__main__':
        main()
