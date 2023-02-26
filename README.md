<img style="display:block; margin-left:auto; margin-right:auto;"
src="https://raw.githubusercontent.com/ssmv01/ccmd/main/CCMD%20logo.png"></img>

### Spend less time typing commands and more time <u>getting things done</u>.

---

NON-PRODUCTION-READY

[![Latest Release](https://img.shields.io/github/v/release/ssmv01/ccmd?display_name=tag&include_prereleases)](https://github.com/ssmv01/ccmd/releases)
[![CodeFactor](https://www.codefactor.io/repository/github/ssmv01/ccmd/badge)](https://www.codefactor.io/repository/github/ssmv01/ccmd)
[![Build](https://img.shields.io/github/actions/workflow/status/ssmv01/ccmd/pylint.yml)](https://github.com/ssmv01/ccmd/actions)
[![Open Issues](https://img.shields.io/github/issues-raw/ssmv01/ccmd)](https://github.com/ssmv01/ccmd/issues)
[![License](https://img.shields.io/github/license/ssmv01/ccmd?color=blue)](https://github.com/ssmv01/ccmd/)

This project is **Under development & testing**. We would love to hear your opinion on this project. Feel free to test it and provied us your feedback.

Read [CONTRIBUTING.md](https://github.com/ssmv01/ccmd/blob/main/CONTRIBUTING.md) if you want to help us make this project better
or mail me at ssmvmails@gmail.com.

Report bugs at our [issue tracker](https://github.com/ssmv01/ccmd/issues).

<br>

## Table of contents
0. [Requirements](https://github.com/SSMV01/ccmd#requirements)
1. [Installation](https://github.com/SSMV01/ccmd#installation)
2. [Usage](https://github.com/SSMV01/ccmd#usage)
    - [Creating a new cutom command](https://github.com/SSMV01/ccmd#creating-a-new-custom-command)
        - [Writing your commands directly into cmds.csv](https://github.com/SSMV01/ccmd#writing-your-commands-directly-into-the-cmdscsv-file)
        - [Creating commands from terminal](https://github.com/SSMV01/ccmd#creating-commands-from-terminal)
        - [Check-if commands](https://github.com/SSMV01/ccmd#check-if-commands)
    - [Using Your Commands](https://github.com/SSMV01/ccmd#using-your-commands)
        - [Using --output and --output-silent](https://github.com/SSMV01/ccmd#using---output-and---output-silent)
    - [Opening the csv file](https://github.com/SSMV01/ccmd#opening-the-csv-file)
    - [Setting the location of the csv file](https://github.com/SSMV01/ccmd#setting-the-location-of-the-csv-file)
    - [List commands](https://github.com/SSMV01/ccmd#list-commands)
    - [Removing commands](https://github.com/SSMV01/ccmd#removing-commands)
    - [Display version](https://github.com/SSMV01/ccmd#display-version)
3. [Uninstallation](https://github.com/SSMV01/ccmd#uninstallation)
4. [Exit codes](https://github.com/SSMV01/ccmd#exit-codes)
5. [Info](https://github.com/SSMV01/ccmd#info)

<br>

## Requirements
### - Linux based OS
### - Python 3 (>= 3.10 recommend)
#### Note: Other operating systems will be supported very soon.

<br>

# Installation

Visit [https://ssmv01.github.io/getccmd](https://ssmv01.github.io/getccmd) and install the `get_ccmd.py` file

Then, open the terminal where you have the file stored and execute the file with:

```
python3 get_ccmd.py
```

*This application is **not** production ready

# Usage

## Creating a new custom command

### Writing your commands directly into the cmds.csv file
<br>

1: Open the csv file:

```
ccmd --opencsv
```

2: Write the Actual Commands first, then the Command Name seperated by a comma as shown below:


```
Actual Command#1 , Command_name#1
Actual Command#2 , Command_name#2
...
...
```
USE `_` underscores for spaces in *Command names*

**Write only one pair of command per row.**


3: Save and close the file once you are done.

<br>

### Creating commands from terminal
<br>

1: Use *--new*:

```
ccmd --new
```

2: Enter the values for the inputs:

```
Actual Command: [Actual Command]
Command Name: [Command name]
```

Using `_` underscores here is not necessary

3: Press **Enter** to save

<br>

### Check-if commands


If output is equal to:

```
command ?= string || command , Command_Name
```

If output contains:

```
command ?: string || command , Command_name
```

#### Explaination
- the first *command* is the command you want to initially run when you execute the custom command

- *?=* checks if the output of the first *command* is equal to string passed after *?=*

- *?:* checks if the output of the first *command* contains the string passed after *?:*

- After the *?= or ?:* give the string that you want to check in *or* compare with the output

- || executes the command given after it IF the condition is True

- Finally, write the command that you want to execute if the condition is true


<br>

## Using your commands
#### Note: All commands with the same name will be executed.

<br>

```
ccmd [command#1] [command#2] ...
```

<br>

### Using --output and --output-silent

`--output` = write to file and execute

```
ccmd [command(s)] --output [path to file]
```
You can replace `--output` with `-o`

`--output-silent` = write to file

```
ccmd [command(s)] --output-silent [path to file]
```

You can replace `--output-silent` with `-oS`

<br>

## Opening the csv file

```
ccmd --opencsv
```

<br>

## Setting the location of the csv file

```
ccmd --setcsv [Path to csv file]
```

If you don't have a specific csv file you want to use:

```
ccmd --setcsv default
```

<br>

## List commands

```
ccmd --list
```

OR

```
ccmd -l
```

If command names are in blue they are '[check_if commands](https://github.com/ssmv01/ccmd#check-if-commands)'

## Removing commands

#### This feature will be added very soon.

For Now:

```
ccmd --opencsv
```

Find and Erase the row. (Try Ctrl + F if you are using a graphical editor)

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

```
cd ~/.ccmd

bash uninstall.sh
```

Do not use _sudo_ here

<br>

# Exit codes

`0`: Execution completed without errors

`1`: Keyboard interrupt

`2`: Execution failed

---

### Info

Version: 0.3.6-alpha

Author: [SSMV01](https://github.com/SSMV01)

MIT License
