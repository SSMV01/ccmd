import sys
import logging


# global
def keyboard_interrupt():
    print()
    logging.info("Exiting...")
    sys.exit(1)


def file_not_found(file):
    logging.error("%s: file not found", file)
    sys.exit(2)


# run_cmd.py
def command_not_found(command):
    logging.error("%s: command not found", command)


# compiler.py
# (se = syntax error)
def se_missing_run(command):
    logging.error("%s: syntax error: missing |=|", command)


def se_missing_if(command):
    logging.error("%s: syntax error: missing if= or if:", command)


# get_input.py
def empty_field():
    logging.warning("this field cannot be empty")
