import sys


def help_message():
    print("""Usage: ccmd [option VALUE] /OR/ [command(s)] [option(s)]
    \nTo open the commands.csv file use 'ccmd' without any arguments
    \nOptions:
    --new                         Create a custom new command
    --setcsv                      Set the location of the csv file
    -o          --output          Write output of command(s) to file AND execute them
    -os         --output-silent   Write output of command(s) to file
    -h          --help            Displays this message
    -v          --version         Display the version number
    --update                     Get the latest changes made to the repository
    --uninstall                  Uninstall ccmd
    \nSee 'manual' located in '~/.ccmd' for more information
    \nv0.4.4-alpha""")
    sys.exit(0)
