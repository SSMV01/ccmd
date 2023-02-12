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
parser = argparse.ArgumentParser(
    prog='ccmd',
    description="command automation tool.",
    add_help=False
    )

VERSION = 'ccmd 0.2.8-alpha'
USERNAME = os.environ.get('LOGNAME')

try:
    with open(f'/home/{USERNAME}/ccmd/bin/cmds_target.txt', 'r', encoding='utf-8') as target_file:
        csv_file = target_file.read()
except FileNotFoundError:
    logging.error(f"Could not find 'cmds_target' at /home/{USERNAME}/ccmd/bin/cmds_target.")
    logging.info("Check if file has been deleted or moved or renamed.")
    sys.exit(2)

parser.add_argument('-h', '--help', help="Display help message", action='store_true')
parser.add_argument('-v', '--version', help="Display version number", action='store_true')
parser.add_argument('--opencsv', help="Open your csv file", action='store_true')
parser.add_argument('--new', help="Create new custom command", action='store_true')
parser.add_argument('--target', type=str, help="Set target csv file")
parser.add_argument('-o', '--output', type=str, help="Write output to file and execute the command")
parser.add_argument('-oS', '--output-silent', type=str, help="Write output to file")
args, commands = parser.parse_known_args()

def main():
    if args.help:
        help()
    elif args.version:
        print(VERSION)
        sys.exit(0)
    elif args.target:
        set_target_file(args.target)

    if csv_file.isspace() or csv_file == '':
        logging.error("No file specified in 'cmds_target.txt'.")
        logging.info("Use '--target' to specify the location of the csv file.")
        sys.exit(2)
    elif args.opencsv:
        os.system(f'editor {csv_file}')
        sys.exit(0)
    elif args.new:
        create_command(csv_file)
    elif commands:
        run_command(csv_file, args.output, args.output_silent)


if len(sys.argv) == 1:
    help()
else:
    if __name__ == '__main__':
        main()
