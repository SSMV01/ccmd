import sys
import csv
import logging
from datetime import datetime
from utils import (rm_space)
from utils import (compile_command, compile_command_for_output, compile_command_no_errs)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

def write_to_file(output_file, command_name, command):
    with open(output_file, 'a') as f:
        f.writelines('\n')
        f.writelines('-' * 75)
        f.writelines( '\n' + command_name + ':')
        f.writelines(f"\nStart time: {datetime.now()}\n")
        f.writelines('\n')
        output = compile_command_for_output(command)
        f.writelines(output + '\n')
        f.writelines('-' * 75)


def run_command(csv_file):
    try:
        if '-o' in sys.argv or '-oS' in sys.argv:
            if len(sys.argv) <= 3:
                logging.error("No commands provided.")
                sys.exit(2)

        for arg in range(1, len(sys.argv)):
            # Replace spaces with _ (underscores)
            usr_inp = rm_space(sys.argv[arg]) if ' ' in sys.argv[arg] else sys.argv[arg]
            notfnd = []
            rowno = 0

            with open(csv_file, 'r') as f:
                csvreader = csv.reader(f)

                for row in csvreader:
                    if usr_inp == row[1].strip():
                        if '-oS' in sys.argv:
                            output_file = sys.argv[-1]
                            write_to_file(output_file, row[1], row[0])
                            sys.exit(0)
                        elif '-o' in sys.argv:
                            output_file = sys.argv[-1]
                            write_to_file(output_file, row[1], row[0])
                        compile_command(row[0])
                    else:
                        notfnd.append('e')
                    rowno += 1
            # if (command not found) error in every row
            if len(notfnd) == rowno:
                logging.error(f"Command '{sys.argv[arg]}' not found!")
                logging.info("Use '-new' to create commands")
        sys.exit(0)

    except IndexError:
        logging.error(f"Syntax error: MISSING ',' in {csv_file}")
        sys.exit(2)

    except FileNotFoundError:
        logging.error(f"{csv_file}: File Not Found!")
        sys.exit(2)

    except KeyboardInterrupt:
        logging.warn("Exiting...")
        sys.exit(1)
