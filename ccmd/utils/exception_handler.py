import sys
import colorama
from colorama import Fore


colorama.init(autoreset=True)

def print_info(x):
    print(Fore.BLUE + "INFO: " + Fore.RESET + x)


def print_err(x):
    print(Fore.RED + "ERROR: " + Fore.RESET + x)


def print_warn(x):
    print(Fore.YELLOW + "WARNING: " + Fore.RESET + x)


# global
def keyboard_interrupt():
    print()
    print_info("Exiting...")
    sys.exit(1)


def file_not_found(file):
    print_err(f"{file}: file not found")
    sys.exit(2)


# customcmd.py
def csv_not_specified():
    print_err("csv file not specified")
    sys.exit(2)


# run_cmd.py
def command_not_found(command):
    print_err(f"{command}: command not found")


# compiler.py
# (se = syntax error)
def se_missing_run(command):
    print_err(f"{command}: syntax error: missing run:")


def se_missing_if(command):
    print_err(f"{command}: syntax error: missing if= or if:")


# get_input.py
def empty_field():
    print_warn("this field cannot be empty")
