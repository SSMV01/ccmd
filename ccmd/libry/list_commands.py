import csv
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def list_command_names(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        file_content = csv.reader(csvfile)
        row_no = 1

        for row in file_content:
            if len(row) < 2:
                continue
            if '?:' in row[0] or '?=' in row[0]:
                print(Fore.BLUE + row[1])
            else:
                print(row[1])
            row_no += 1
