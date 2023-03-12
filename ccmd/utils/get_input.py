import logging
import readline
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")

def check_input(inp: str):
    return 1 if inp == '' or inp.isspace() else 0

def rm_space(inp: str):
    inp = inp.split(' ')
    final_inp = '_'
    return final_inp.join(inp)

def get_and_check(msg):
    got_input = input(f'{msg}: ').strip()
    readline.add_history(got_input)
    if check_input(got_input) == 0:
        return got_input
    logging.error("This field cannot be empty.")
    return ''

def get_and_check_nospace(msg):
    got_input = input(f'{msg}: ').strip()
    if check_input(got_input) == 0:
        if ' ' in got_input:
            got_input = rm_space(got_input)
        return got_input
    logging.error("This field cannot be empty.")
    return ''

def get_the_input(msg):
    got_input = get_and_check(msg)
    while got_input == '':
        got_input = get_and_check(msg)
    return got_input

def nospace_input(msg):
    got_input = get_and_check_nospace(msg)
    while got_input == '':
        got_input = get_and_check_nospace(msg)
    return got_input
