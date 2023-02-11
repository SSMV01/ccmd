import sys

def help():
    print("""Basic Usage: ccmd [command(s)] [option(s)]
    \nUsage: ccmd <option VALUE> [command(s)] [option(s)]
    \nType: ccmd --help [option name]\nFor more information about the option.
    \nOptions:
    --new          Create a custom new command.
    --opencsv     Open the cmds.csv file.
    --target      Set the location of the csv file.
    -o            Write output of command(s) to file AND execute them.
    -oS           Write output of command(s) to file.
    -h            Displays this message.
    --help        Same as -h.
    -v            Display the version number.
    --version     Same as -v.
    \nSee: 'https://github.com/SSMV01/CustomCmd/blob/main/README.md' for more information.""")
    sys.exit(0)
