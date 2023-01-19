#!/usr/bin/python3

import os
import sys
import logging
from libry import (create_command, set_target_file,  run_command, write_output, write_output_silent, help)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

try:
    with open(f'/home/{os.getlogin()}/customcmd/bin/cmds_target.txt', 'r') as target_file:
        csv_file = target_file.read()
except FileNotFoundError:
    logging.error(f"Could not find 'cmds_target' at /home/{os.getlogin()}/customcmd/bin/cmds_target.")
    logging.info("Check if file has been deleted or moved or renamed.")
    sys.exit(2)
    
    

def main():
    if '-h' in sys.argv or '--help' in sys.argv:
        help()
        sys.exit(0)
    elif '--target' in sys.argv:
        set_target_file()
        sys.exit(0)
    elif '--opencsv' in sys.argv:
        os.system(f'xdg-open {csv_file}')
        sys.exit(0)

    if csv_file.isspace() or csv_file == '':
        logging.error("No file specified in 'cmds_target.txt'.")
        logging.info("Use '--target' to specify the location of the csv file.")
        sys.exit(2)
    elif '-new' in sys.argv:
        create_command(csv_file)
        sys.exit(0)
    elif '-o' in sys.argv:
        write_output(csv_file)
        sys.exit(0)
    elif '-oS' in sys.argv:
        write_output_silent(csv_file)
        sys.exit(0)
    else:
        run_command(csv_file)
        sys.exit(0)


if len(sys.argv) < 2:
    logging.error("No Input given.")
    logging.info("Type 'ccmd --help' for usage info.")
    sys.exit(2)
else:
    if __name__ == '__main__':
        main()