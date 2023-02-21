import os
import logging
from subprocess import Popen, PIPE
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")

# Executes the first command; then checks if the output is equal to/contains the user provided string
# if yes then executes the second command too.

def if_equals(cmd: str):
    split_if = cmd.split('?=') # ["first command", "string & second command"]
    split_run = split_if[1].split('||') # ["string", "second command"]
    check_out = Popen(split_if[0].split(), stdout=PIPE) # check output of first command
    output = check_out.stdout.read() # read output
    output = str(output.strip(), 'utf-8') # extract output

    os.system(split_if[0].strip()) # run first command
    if output == split_run[0].strip(): # if output  of first command == the string
        os.system(split_run[1].strip()) # run second command

def if_contains(cmd: str):
    split_if = cmd.split('?:')
    split_run = split_if[1].split('||')
    check_out = Popen(split_if[0].split(), stdout=PIPE)
    output = check_out.stdout.read()
    output = str(output.strip(), 'utf-8')

    os.system(split_if[0].strip())
    if split_run[0].strip() in output: # if output  of first command contains the string
        os.system(split_run[1].strip())

# if it is a complex command; make sure the syntax is correct
# else just execute the command

def compile_command(cmd: str):
    if '?=' in cmd and '||' in cmd:
        if_equals(cmd)
    elif '?:' in cmd and '||' in cmd:
        if_contains(cmd)
    elif '?=' in cmd or '?:' in cmd and '||' not in cmd:
        logging.error("Syntax error in '%s': missing ||", cmd)
    elif '||' in cmd and '?:' not in cmd and '?=' not in cmd:
        logging.error("Syntax error in '%s': missing ?: OR ?=", cmd)
    else:
        os.system(cmd)

# For -o and -oS
# Returns output of the first command; then checks if the output is equal to/contains the user provided string
# if yes then returns the output of second command too.

def if_equals_for_output(cmd: str):
    split_if = cmd.split('?=')
    split_run = split_if[1].split('||')
    check_out1 = Popen(split_if[0].split(), stdout=PIPE)
    output1 = check_out1.stdout.read()
    output1 = str(output1.strip(), 'utf-8')

    if output1 == split_run[0].strip():
        check_out2 = Popen(split_run[1].split(), stdout=PIPE)
        output2 = check_out2.stdout.read()
        output2 = str(output2.strip(), 'utf-8')
    else:
        output2 = f"output is not equal to '{split_run[0].strip()}'"

    return f"{output1}\n\n{output2}"

def if_contains_for_output(cmd: str):
    split_if = cmd.split('?:')
    split_run = split_if[1].split('||')
    check_out1 = Popen(split_if[0].split(), stdout=PIPE)
    output1 = check_out1.stdout.read()
    output1 = str(output1.strip(), 'utf-8')

    if split_run[0].strip() in output1:
        check_out2 = Popen(split_run[1].split(), stdout=PIPE)
        output2 = check_out2.stdout.read()
        output2 = str(output2.strip(), 'utf-8')
    else:
        output2 = f"output does not contain '{split_run[0].strip()}'"

    return f"{output1}\n\n{output2}"

# if it is a complex command; make sure the syntax is correct
# else just return the output

def compile_command_for_output(cmd: str):
    if '?=' in cmd and '||' in cmd:
        return if_equals_for_output(cmd)
    elif '?:' in cmd and '||' in cmd:
        return if_contains_for_output(cmd)
    elif '?=' in cmd or '?:' in cmd and '||' not in cmd:
        return "[-] Syntax Err: missing ||"
    elif '||' in cmd and '?:' not in cmd and '?=' not in cmd:
        return "[-] Syntax Err: missing ?: OR ?="
    output = Popen(cmd.split(), stdout=PIPE)
    output = output.stdout.read()
    output = str(output.strip(), 'utf-8')
    return output