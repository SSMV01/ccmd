## CCMD

[![Latest Release](https://img.shields.io/github/v/release/SSMV01/ccmd?display_name=tag&include_prereleases)](https://github.com/SSMV01/ccmd/releases)
[![CodeFactor](https://www.codefactor.io/repository/github/ssmv01/ccmd/badge)](https://www.codefactor.io/repository/github/ssmv01/ccmd)
[![Build](https://img.shields.io/github/actions/workflow/status/SSMV01/ccmd/pylint.yml)](https://github.com/SSMV01/ccmd/actions)
[![Open Issues](https://img.shields.io/github/issues-raw/SSMV01/ccmd)](https://github.com/SSMV01/ccmd/issues)
[![License](https://img.shields.io/github/license/SSMV01/ccmd?color=blue)](https://github.com/SSMV01/ccmd/)

### customcmd

### This program is under development

## Requirements

- ### Python3
- ### Linux

# Installation
1: Download the source code from [releases](https://github.com/SSMV01/ccmd/releases) and save it at the _/home/(user)/_ directory as _ccmd_
### Note:
- Saving the folder as 'ccmd' is a necessity.
- Saving the ccmd folder at _/home/(user)/_ is a necessity.

2: `cd` into the _ccmd_ directory:

```
cd ccmd
```

3: Run the _init.sh_ file with `bash`:

```
sudo bash init.sh
```

`sudo` is necessary to access the _/bin_ folder

4 : Set your target file (csv file)'s path.
See: [Setting the location of the csv file](https://github.com/SSMV01/ccmd/#setting-the-location-of-the-csv-file)

And you're all set!

# Usage

Basic Usage:

```
ccmd [command(s)] [option(s)...]
```

## Creating a New Custom Command

<br>

### Note: If you create multiple commands with the same name they will all be executed when you run the command.

<br>

### Writing your command directly into the cmds.csv file
<br>

---

#### Syntax

```
Actual Command,Your_command_name
```

USE `_(s)` underscores for spaces ONLY for _Your command name_s

---

<br>

<br>

1: Open the _cmds.csv_ file located in the _ccmd/bin_ folder

See: [Opening the cmds.csv file from the terminal](https://github.com/SSMV01/CCMD#opening-the-cmdscsv-file-from-the-terminal)

2: Write the Actual Commands first, then Your command seperated by a comma.
__Write only one pair of command per row.__

```
Actual Command#1,Your_Command_name#1
Actual Command#2,Your_Command_name#2
...
...
```
USE `_(s)` underscores for spaces ONLY for _Your command name_s
3: Save and close the file once you are done.

<br>

### Creating commands from terminal
<br>

1: Use _--new_:

```
ccmd --new
```

2: Enter the values for the inputs:

```
Actual Command: <Command To Replace>
Command Name: <Your Command name>
```

You dont have to use `_(s)` underscores for spaces here in _Command Name_

3: Press __Enter__ to save.

### Check Output and run commands
Write these commands in the _cmds.csv_ file or when you run _--new_
You can only use this feature in the _Actual commands_ part
Syntax:

If output is equal to:

```
Actual Command ?= string to compare with output || command to run if output equals the given string,Your_Command_name
```

If output contains:

```
Actual Command ?: string to check in output || command to run if output contains the given string,Your_Command_name
```

### Explaination
- _Actual Command_ is the command you want to initially run when you execute the custom command
- _?=_ checks if the output of the _Actual Command_ is equal to string passed after _?=_
- _?:_ checks if the output of the _Actual Command_ contains the string passed after _?:_
- After the _?= or ?:_ give the string that you want to check in _or_ compare with the output
- || executes the command given after it IF the condition is TRUE
- Finally, write the command that you want to execute if the condition is true


<br>

## Using Your Commands

<br>

### Note: If you have multiple commands with the same name they will all be executed when you run the command.

<br>

Note: Its not necessary to use `_(s)` underscores for spaces here but you can do so to avoid the usage of `""`

```
ccmd <Your Command>
```
__If your command contains space use double quotes or `_(s)`underscores:__

```
ccmd "<Your Command>"
```
OR

```
ccmd Your_Command
```
### Using multiple commands
<br>

```
ccmd <command#1> <command#2> ...
```

### Using -o and -oS
<br>

 _-o_ writes the output(s) to the specified file __AND__ also runs the command in your terminal.

```
ccmd <command(s)> -o <out_file>
```

 _-oS_ writes the output(s) to the specified file but __DOES NOT__ run the command in your terminal.

```
ccmd <command(s)> -oS <out_file>
```

<br>

## Opening the cmds.csv file from the terminal

We recommend you to use a text editor to open the csv file instead of excel like software.

```
ccmd --opencsv
```

<br>

## Setting the location of the csv file

```
ccmd --target <Path to csv file>
```

If you don't have a specific csv file you want to use:

```
ccmd --target default
```

<br>

## Removing Commands

1. Open the _cmds.csv_ file

```
ccmd --opencsv
```

2. Find and Erase the row.

<br>

## Display version

```
ccmd -v
```

OR

```
ccmd --version
```

<br>

# Uninstallation

Run the _uninstall.sh_ file located in the _ccmd_ directory

```
bash uninstall.sh
```

Do not use _sudo_ here

---
<br>

### Info
_Version_: 0.2.8-alpha
_Author_: [SSMV01](https://github.com/SSMV01)
MIT License
