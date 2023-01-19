import logging
# Initialize logging
logging.basicConfig(format="%(levelname)s: %(message)s")

def check_input(inp=''):
    if inp == '' or inp.isspace():
        return 1
    else:
        return 0

def rm_space(inp=''):
    inp = inp.split(' ')
    final_inp = '_'
    final_inp = final_inp.join(inp)
    return final_inp

def get_and_check(msg):
    print(msg + ': ')
    got_input = input().strip()
    if check_input(got_input) == 0:
        return got_input
    else:
        logging.error("This field cannot be empty.")
        return ''

def get_and_check_nospace(msg):
    print(msg + ': ')
    got_input = input().strip()
    if check_input(got_input) == 0:
        if ' ' in got_input:
            got_input = rm_space(got_input)
        return got_input
    else:
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