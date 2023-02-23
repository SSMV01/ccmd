#!/usr/bin/python3
import os
import sys
import logging
import argparse
from libry import (create_command, set_csv_file, run_command, help, list_command_names)
# Initialize logging
logging.basicConfig(format='%(levelname)s: %(message)s')
logging.getLogger().setLevel(logging.INFO)
#Initialize argparse
parser = argparse.ArgumentParser(
    prog='ccmd',
    description="command automation tool.",
    add_help=False
    )

VERSION = 'ccmd 0.3.2-alpha'
USERNAME = os.environ.get('LOGNAME')

try:
    with open(f'/home/{USERNAME}/ccmd/bin/cmds_target.txt', 'r', encoding='utf-8') as target_file:
        csv_file = target_file.read()
except FileNotFoundError:
    logging.error("Could not find 'cmds_target' at /home/%s/ccmd/bin/.", USERNAME)
    sys.exit(2)

parser.add_argument('-h', '--help', help="Display help message", action='store_true')
parser.add_argument('-v', '--version', help="Display version number", action='store_true')
parser.add_argument('-l', '--list', help="List all commands names in csv", action='store_true')
parser.add_argument('--opencsv', help="Open your csv file", action='store_true')
parser.add_argument('--setcsv', type=str, help="Set target csv file")
parser.add_argument('--new', help="Create new custom command", action='store_true')
parser.add_argument('-o', '--output', type=str, help="Write output to file and execute the command")
parser.add_argument('-oS', '--output-silent', type=str, help="Write output to file")
args, commands = parser.parse_known_args()

def main():
    if args.help:
        help()
    elif args.version:
        print(VERSION)
        sys.exit(0)
    elif args.setcsv:
        set_csv_file(args.setcsv)

    if csv_file.isspace() or csv_file == '':
        logging.error("No file specified in 'cmds_target.txt'.")
        sys.exit(2)
    elif args.opencsv:
        os.system(f'editor {csv_file}')
        sys.exit(0)
    elif args.list:
        list_command_names(csv_file)
    elif args.new:
        create_command(csv_file)
    elif commands:
        run_command(commands, csv_file, args.output, args.output_silent)


if len(sys.argv) == 1:
    help()
else:
    if __name__ == '__main__':
        main()
