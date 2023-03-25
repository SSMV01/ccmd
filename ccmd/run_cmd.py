import sys
import csv
import logging
from utils import (rm_space, compile_command, compile_command_for_output)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

def run_command(commands, csv_file: str, output, output_silent):
    try:
        for command in commands:
            # Replaces space with _ (underscore)
            usr_inp = rm_space(command) if ' ' in command else command
            notfnd = []
            rowno = 0

            with open(csv_file, 'r', encoding='utf-8') as csvfile:
                csvreader = csv.reader(csvfile)

                for row in csvreader:
                    if len(row) < 2:
                        continue
                    if usr_inp == row[1].strip():
                        if output_silent:
                            output = False
                            compile_command_for_output(output_silent, row[1], row[0])
                        elif output:
                            output_silent = False
                            compile_command_for_output(output, row[1], row[0])
                            compile_command(row[0])
                        else:
                            compile_command(row[0])
                    else:
                        notfnd.append('e')
                    rowno += 1
            # if (command not found) error in every row
            if len(notfnd) == rowno:
                logging.error("Command %s not found!", command)
                logging.info("Use '--new' to create commands")
        sys.exit(0)

    except FileNotFoundError:
        logging.error("%s: File Not Found!", csv_file)
        sys.exit(2)

    except IsADirectoryError:
        logging.error("%s: File Not Found!", csv_file)

    except KeyboardInterrupt:
        print()
        logging.info("Exiting...")
        sys.exit(1)
