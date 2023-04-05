import sys


def help_message():
    print("""Usage: ccmd <option VALUE> [command(s)] [option(s)]
    \nOptions:
    --new                        Create a custom new command.
    --opencsv                    Open the cmds.csv file.
    --target                     Set the location of the csv file.
    -o         --output          Write output of command(s) to file AND execute them.
    -oS        --output-silent   Write output of command(s) to file.
    -h         --help            Displays this message.
    -v         --version         Display the version number.
    --update                     Get the latest changes made to the repository.
    --uninstall                  Uninstall ccmd.
    \nSee 'manual' folder located in '.ccmd' folder for more information.
    \nv0.4.3-alpha""")
    sys.exit(0)
