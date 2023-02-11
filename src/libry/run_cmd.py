import sys
import csv
import logging
from datetime import datetime
from utils import (rm_space)
from utils import (compile_command, compile_command_for_output)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

def write_to_file(output_file: str, command_name: str, command: str):
    if output_file.isspace() or output_file == '' or output_file == '-o' or output_file == '-oS':
        logging.error("No output file given.")
        sys.exit(2)
    with open(output_file, 'a', encoding='utf-8') as file:
        file.writelines('\n')
        file.writelines('-' * 75)
        file.writelines( '\n' + command_name + ':')
        file.writelines(f"\nStart time: {datetime.now()}\n")
        file.writelines('\n')
        output = compile_command_for_output(command)
        file.writelines(output + '\n')
        file.writelines('-' * 75)


def run_command(csv_file: str):
    try:
        output_used = 0
        output_silent_used = 0
        output_file = sys.argv[-1]

        if '-o' in sys.argv or '-oS' in sys.argv:
            if len(sys.argv) <= 3:
                logging.error("No commands OR file provided.")
                sys.exit(2)
            if '-o' in sys.argv:
                output_used = 1
            elif '-oS' in sys.argv:
                output_silent_used = 1
            sys.argv.pop()
            sys.argv.pop()

        for arg in range(1, len(sys.argv)):
            # Replace spaces with _ (underscores)
            usr_inp = rm_space(sys.argv[arg]) if ' ' in sys.argv[arg] else sys.argv[arg]
            notfnd = []
            rowno = 0

            with open(csv_file, 'r', encoding='utf-8') as f:
                csvreader = csv.reader(f)

                for row in csvreader:
                    if len(row) < 2:
                        continue
                    if usr_inp == row[1].strip():
                        if output_silent_used == 1:
                            write_to_file(output_file, row[1], row[0])
                            sys.exit(0)
                        elif output_used == 1:
                            write_to_file(output_file, row[1], row[0])
                        compile_command(row[0])
                    else:
                        notfnd.append('e')
                    rowno += 1
            # if (command not found) error in every row
            if len(notfnd) == rowno:
                logging.error(f"Command '{sys.argv[arg]}' not found!")
                logging.info("Use '--new' to create commands")
        sys.exit(0)

    except FileNotFoundError:
        logging.error(f"{csv_file}: File Not Found!")
        sys.exit(2)

    except IsADirectoryError:
        logging.error(f"{csv_file}: File Not Found!")

    except KeyboardInterrupt:
        logging.info("Exiting...")
        sys.exit(1)
