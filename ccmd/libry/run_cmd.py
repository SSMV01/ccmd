import sys
import csv
import logging
from datetime import datetime
from utils import (rm_space, compile_command, compile_command_for_output)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

def write_to_file(output_file: str, command_name: str, command: str):
    if output_file.isspace() or output_file == '' or output_file == '-o' or output_file == '-oS':
        logging.error("No output file given.")
        sys.exit(2)
    with open(output_file, 'a', encoding='utf-8') as file:
        file.writelines('\n')
        file.writelines(f'\nCommand {command_name}\n')
        file.writelines('-' * 20)
        file.writelines(f"\nStart time: {str(datetime.now()).split('.', maxsplit=1)[0]}\n")
        file.writelines('\n')
        output = compile_command_for_output(command)
        file.writelines(output + '\n')


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
                            write_to_file(output_silent, row[1], row[0])
                        elif output:
                            output_silent = False
                            write_to_file(output, row[1], row[0])
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
        logging.info("Exiting...")
        sys.exit(1)
