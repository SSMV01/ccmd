#!/usr/bin/python3

import os
import sys
import argparse

from uninstall_ccmd import uninstall
from update import get_update
from help_msg import help_message
from set_csv import set_csv_file
from list_commands import list_command_names
from create_cmd import create_command
from run_cmd import run_command
from utils import exception_handler


# Initialize argparse
parser = argparse.ArgumentParser(
    prog='ccmd',
    description="command automation tool.",
    add_help=False
)

VERSION = 'ccmd v0.4.4-alpha'
USERNAME = os.environ.get('LOGNAME')

try:
    with open(f'/home/{USERNAME}/.ccmd/data/cmds_target.txt', 'r', encoding='utf-8') as target_file:
        csv_file = target_file.read()
except FileNotFoundError:
    exception_handler.print_err(f"could not find 'cmds_target' at /home/{USERNAME}/.ccmd/data/.")
    sys.exit(2)

parser.add_argument('--uninstall', help="Uninstall ccmd", action='store_true')
parser.add_argument('--update', help="Update ccmd to latest release", action='store_true')
parser.add_argument('-h', '--help', help="Display help message", action='store_true')
parser.add_argument('-v', '--version', help="Display version number", action='store_true')
parser.add_argument('--setcsv', type=str, help="Set target csv file")
parser.add_argument('-l', '--list', help="List all commands names in csv", action='store_true')
parser.add_argument('--new', help="Create new custom command", action='store_true')
parser.add_argument('-o', '--output', type=str, help="Write output to file and execute the command")
parser.add_argument('-os', '--output-silent', type=str, help="Write output to file")
options, commands = parser.parse_known_args()


def main():
    if options.uninstall:
        uninstall()
    elif options.update:
        get_update()
    elif options.help:
        help_message()
    elif options.version:
        print(VERSION)
        sys.exit(0)
    elif options.setcsv:
        set_csv_file(options.setcsv)

    if csv_file.isspace() or csv_file == '':
        exception_handler.csv_not_specified()
    elif options.list:
        list_command_names(csv_file)
    elif options.new:
        create_command(csv_file)
    elif commands:
        # Note: we are providing the values passed with -o or -oS here
        run_command(commands, csv_file, options.output, options.output_silent)


if len(sys.argv) == 1:
    if csv_file.isspace() or csv_file == '':
        exception_handler.csv_not_specified()
    os.system(f'editor {csv_file}')
    sys.exit(0)
else:
    if __name__ == '__main__':
        main()
