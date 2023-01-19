def help():
    print("""Usage: ccmd [command(s)] [option(s)...]
\nNote: Make sure to use "" (quotes) if your commands contain ' ' (space)
OR you can use _ (underscores) for spaces.
    \nType: ccmd --help [option name]
For more information about the option.
    \nOptions:
    -new          Create a custom new command.
    --opencsv     Open the cmds.csv file.
    --target      Set the location of the csv file.
    -o            Write output of command(s) to file AND execute them.
    -oS           Write output of command(s) to file.
    -h            Displays this message.
    --help        Same as -h.
    \nSee: 'https://github.com/SSMV01/CustomCmd/blob/main/README.md' for more information.""")
    
def new_help():
    print("""Usage: ccmd -new
Note: No other arguments are required.
        """)

def opencsv_help():
    print("""Usage: ccmd --opencsv
Note: No other arguments are required.
        """)

def target_help():
    print("""Usage: ccmd --target [csv_file path]
Note: Use "" (quotes) if the path contains a ' ' (space).
        """)
    
def output_help():
    print("""Usage: ccmd [command(s)] -o [txt_file path]
Note: Use "" (quotes) if the path contains a ' ' (space).
        """)

def output_silent_help():
    print("""Usage: ccmd [command(s)] -oS [txt_file path]
Note: Use "" (quotes) if the path contains a ' ' (space).
        """)