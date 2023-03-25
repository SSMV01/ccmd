import os
import sys
import logging
from datetime import datetime
from subprocess import Popen, PIPE
import colorama
from colorama import Fore
# Initialize colorama
colorama.init(autoreset=True)
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")

def split_next(cmd: str):
    return cmd.split('next>')


# Executes the first command; then checks if the output is equal to/contains the user provided string
# if yes, then executes the second command too.

def if_equals(cmd: str):
    split_if = cmd.split('if=') # ["first command", "string & second command"]
    split_run = split_if[1].split('|=|') # ["string", "second command"]
    check_out = Popen(split_if[0].split(), stdout=PIPE) # check output of first command

    print(Fore.GREEN + split_if[0].strip()) # Print command name
    print(Fore.BLUE + '-' * 20)
    os.system(split_if[0].strip()) # run first command
    output = check_out.stdout.read() # read output
    output = str(output.strip(), 'utf-8') # remove unwanted chars

    if output == split_run[0].strip(): # if output  of first command == the string
        print(Fore.GREEN + split_run[1].strip()) # Print command name
        print(Fore.BLUE + '-' * 20)
        os.system(split_run[1].strip()) # run second command
        print()


def if_contains(cmd: str):
    split_if = cmd.split('if:')
    split_run = split_if[1].split('|=|')
    check_out = Popen(split_if[0].split(), stdout=PIPE)

    print(Fore.GREEN + split_if[0].strip())
    print(Fore.BLUE + '-' * 20)
    os.system(split_if[0].strip())
    output = check_out.stdout.read()
    output = str(output.strip(), 'utf-8')

    if split_run[0].strip() in output: # if output of first command contains the string
        print(Fore.GREEN + split_run[1].strip())
        print(Fore.BLUE + '-' * 20)
        os.system(split_run[1].strip())
        print()


# if it is a check-if command; if the syntax is correct: execute the command
# else just execute the command

def compile_command(cmd: str):
    cmd = split_next(cmd)
    print(cmd)

    for command in cmd:
        if 'if=' in command and '|=|' in command:
            if_equals(command)
        elif 'if:' in command and '|=|' in command:
            if_contains(command)
        elif 'if=' in command or 'if:' in command and '|=|' not in command:
            logging.error("Syntax error in '%s': missing |=|", command)
        elif '|=|' in command and 'if:' not in command and 'if=' not in command:
            logging.error("Syntax error in '%s': missing if: OR if=", command)
        else:
            print(Fore.GREEN + command)
            print(Fore.BLUE + '-' * 20)
            os.system(command)
            print()


# For -o and -oS
# Returns output of the first command; then checks if the output is equal to/contains the user provided string
# if yes, then returns the output of second command too.

def if_equals_for_output(cmd: str):
    split_if = cmd.split('if=')
    split_run = split_if[1].split('|=|')

    with Popen(split_if[0].split(), stdout=PIPE) as check_out1:
        output1 = check_out1.stdout.read()
        output1 = str(output1.strip(), 'utf-8')

    if output1 == split_run[0].strip():
        with Popen(split_run[1].split(), stdout=PIPE) as check_out2:
            output2 = check_out2.stdout.read()
            output2 = str(output2.strip(), 'utf-8')
    else:
        output2 = f"output is not equal to '{split_run[0].strip()}'"

    return f"{output1}\n\n{output2}"


def if_contains_for_output(cmd: str):
    split_if = cmd.split('if:')
    split_run = split_if[1].split('|=|')

    with Popen(split_if[0].split(), stdout=PIPE) as check_out1:
        output1 = check_out1.stdout.read()
        output1 = str(output1.strip(), 'utf-8')

    if split_run[0].strip() in output1:
        with Popen(split_run[1].split(), stdout=PIPE) as check_out2:
            output2 = check_out2.stdout.read()
            output2 = str(output2.strip(), 'utf-8')
    else:
        output2 = f"output does not contain '{split_run[0].strip()}'"

    return f"{output1}\n\n{output2}"


# if it is a check-if command; if the syntax is correct: return output
# else just return the output

def write_to_file(output_file: str, command_name: str, output: str):
    if output_file.isspace() or output_file == '' or output_file == '-o' or output_file == '-oS':
        logging.error("No output file given.")
        sys.exit(2)
    with open(output_file, 'a', encoding='utf-8') as file:
        file.writelines('\n')
        file.writelines(f'\nCommand {command_name}\n')
        file.writelines('-' * 20)
        file.writelines(f"\nStart time: {str(datetime.now()).split('.', maxsplit=1)[0]}\n")
        file.writelines('\n')
        file.writelines(output + '\n')


def compile_command_for_output(output_file: str, command_name: str, cmd: str):
    cmd = cmd.split('next>')

    for command in cmd:
        if 'if=' in command and '|=|' in command:
            output = if_equals_for_output(command)
            write_to_file(output_file, command_name, output)
        elif 'if:' in command and '|=|' in command:
            output = if_contains_for_output(command)
            write_to_file(output_file, command_name, output)
        elif 'if=' in command or 'if:' in command and '|=|' not in command:
            output = "[-] Syntax Err: missing |=|"
            write_to_file(output_file, command_name, output)
        elif '|=|' in command and 'if:' not in command and 'if=' not in command:
            output = "[-] Syntax Err: missing if: OR if="
            write_to_file(output_file, command_name, output)
        else:
            with Popen(command.split(), stdout=PIPE) as check_output:
                output = check_output.stdout.read()
                output = str(output.strip(), 'utf-8')
            write_to_file(output_file, command_name, output)
