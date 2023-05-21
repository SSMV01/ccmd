import sys
import csv

from pathlib import Path
from utils import get_the_input, nospace_input, exception_handler


def create_command(csv_file):
    try:
        if Path(csv_file).is_file():
            actual_cmd = get_the_input("command")
            cmd_name = nospace_input("command name")

            cmd_lst = [actual_cmd, cmd_name]

            with open(csv_file, 'a', newline='', encoding='utf-8') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(cmd_lst)

                exception_handler.print_info("command created.")

            sys.exit(0)

        else:
            exception_handler.file_not_found(csv_file)

    except KeyboardInterrupt:
        exception_handler.keyboard_interrupt()
