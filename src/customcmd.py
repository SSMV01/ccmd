#!/usr/bin/python3
import os
import sys
import logging
import argparse
from libry import (create_command, set_target_file, run_command, help)
# Initialize logging
logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)
#Initialize argparse
parser = argparse.ArgumentParser(prog='ccmd', description="command automation tool.", add_help=False)

version = 'ccmd 0.2.5-alpha'
username = os.environ.get('LOGNAME')

try:
    with open(f'/home/{username}/ccmd/bin/cmds_target.txt', 'r') as target_file:
        csv_file = target_file.read()
except FileNotFoundError:
    logging.error(f"Could not find 'cmds_target' at /home/{username}/customcmd/bin/cmds_target.")
    logging.info("Check if file has been deleted or moved or renamed.")
    sys.exit(2)

parser.add_argument('-h', '--help', help="Display help message", action='store_true')
parser.add_argument('-v', '--version', help="Display version number", action='store_true')
parser.add_argument('--opencsv', help="Open your csv file", action='store_true')
parser.add_argument('--new', help="Create new custom command", action='store_true')
parser.add_argument('--target', type=str, help="Set target csv file")
args, commands = parser.parse_known_args()

def main():
    if args.help:
        help()
    elif args.version:
        print(version)
        sys.exit(0)
    elif args.target:
        set_target_file(args.target)

    if csv_file.isspace() or csv_file == '':
        logging.error("No file specified in 'cmds_target.txt'.")
        logging.info("Use '--target' to specify the location of the csv file.")
        sys.exit(2)
    elif args.opencsv:
        os.system(f'xdg-open {csv_file}')
        sys.exit(0)
    elif args.new:
        create_command(csv_file)
    elif commands:
        run_command(csv_file)


if len(sys.argv) == 1:
    help()
else:
    if __name__ == '__main__':
        main()
