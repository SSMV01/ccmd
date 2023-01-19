import sys
import csv
import logging
from datetime import datetime
from utils import (rm_space)
from utils import (compile_command, compile_command_for_output, compile_command_no_errs)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

def run_command(csv_file):
    try:
        for arg in range(1, len(sys.argv)):
            # Replace spaces with _ (underscores)
            if ' ' in sys.argv[arg]:
                usr_inp = rm_space(sys.argv[arg])
            else:
                usr_inp = sys.argv[arg]

            notfnd = []
            rowno = 0

            with open(csv_file, 'r') as f:
                csvreader = csv.reader(f)

                for row in csvreader:
                    if usr_inp == row[1].strip():
                        compile_command(row[0])
                        rowno += 1
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

def write_output(csv_file):
    try:
        for arg in range(1, len(sys.argv) - 2):
            # Replace spaces with _ (underscores)
            if ' ' in sys.argv[arg]:
                usr_inp = rm_space(sys.argv[arg])
            else:
                usr_inp = sys.argv[arg]

            notfnd = []
            rowno = 0

            with open(csv_file, 'r') as f:
                csvreader = csv.reader(f)

                for row in csvreader:
                    if usr_inp == row[1].strip():
                        output_file = sys.argv[-1]
                        with open(output_file, 'a') as f:
                            f.writelines('\n')
                            f.writelines('-' * len(row[0]))
                            f.writelines( '\n' + row[0] + ':')
                            f.writelines(f"\nStart time: {datetime.now()}\n")
                            f.writelines('\n')
                            output = compile_command_for_output(row[0])
                            f.writelines(output + '\n')
                            f.writelines('-' * len(row[0]))
                        compile_command_no_errs(row[0])
                        rowno += 1
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

    except FileNotFoundError as ex:
        logging.error(f"{csv_file}: File Not Found!")
        sys.exit(2)

    except KeyboardInterrupt:
        logging.warn("Exiting...")
        sys.exit(1)

def write_output_silent(csv_file):
    try:
        for arg in range(1, len(sys.argv) - 2):
            # Replace spaces with _ (underscores)
            if ' ' in sys.argv[arg]:
                usr_inp = rm_space(sys.argv[arg])
            else:
                usr_inp = sys.argv[arg]
            notfnd = []
            rowno = 0

            with open(csv_file, 'r') as f:
                csvreader = csv.reader(f)

                for row in csvreader:
                    if usr_inp == row[1].strip():
                        output_file = sys.argv[-1]
                        with open(output_file, 'a') as f:
                            f.writelines('\n')
                            f.writelines('-' * len(row[0]))
                            f.writelines( f'{row[0]}:')
                            f.writelines(f"\nStart time: {datetime.now()}\n")
                            f.writelines('\n')
                            output = compile_command_for_output(row[0])
                            f.writelines(output + '\n')
                            f.writelines('-' * len(row[0]))
                        rowno += 1
                    else:
                        notfnd.append('e')
                        rowno += 1
                
            # if (command not found) error in every row
            if len(notfnd) == rowno:
                logging.error(f"Command '{sys.argv[arg]}' not found!")
                logging.error("Use '-new' to create commands")
        sys.exit(0)
    
    except IndexError:
        logging.error(f"Syntax error: MISSING ',' in {csv_file}")
        sys.exit(2)

    except FileNotFoundError as ex:
        logging.error(f"{csv_file}: File Not Found!")
        sys.exit(2)

    except KeyboardInterrupt:
        logging.error("Exiting...")
        sys.exit(1)