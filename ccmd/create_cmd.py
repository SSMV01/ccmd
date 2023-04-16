import sys
import csv
import logging
from pathlib import Path
from utils import get_the_input, nospace_input, exception_handler

# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)


def create_command(csv_file):
    try:
        if Path(csv_file).is_file():
            actual_cmd = get_the_input("Command")
            cmd_name = nospace_input("Command Name")

            cmd_lst = [actual_cmd, cmd_name]

            with open(csv_file, 'a', newline='', encoding='utf-8') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(cmd_lst)

                logging.info("Command created.")

            sys.exit(0)

        else:
            exception_handler.file_not_found(csv_file)

    except KeyboardInterrupt:
        exception_handler.keyboard_interrupt()
