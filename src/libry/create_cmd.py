import sys
import csv
import logging
from utils import (get_the_input, nospace_input)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

def create_command(csv_file):
    try: 
        actual_cmd = get_the_input("Actual Command")
        replacement_cmd = nospace_input("Replacement Command")

        cmd_lst = [actual_cmd, replacement_cmd]

        with open(csv_file, 'a', newline='') as f:
            csvwriter = csv.writer(f)

            csvwriter.writerow(cmd_lst)
            logging.info("Command created.")

        sys.exit(0)

    except FileNotFoundError:
        logging.error(f'{csv_file}: Not found!')

    except KeyboardInterrupt:
        logging.info("Exiting...")
        sys.exit(1)
