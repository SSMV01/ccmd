<img style="display:block; margin-left:auto; margin-right:auto;"
src="https://raw.githubusercontent.com/SSMV01/ccmd/main/CCMD%20logo.png"></img>

### ccmd is a tool created to help you spend less time typing commands and more time getting things done.

---

[![Latest Release](https://img.shields.io/github/v/release/SSMV01/ccmd?display_name=tag&include_prereleases)](https://github.com/SSMV01/ccmd/releases)
[![CodeFactor](https://www.codefactor.io/repository/github/SSMV01/ccmd/badge)](https://www.codefactor.io/repository/github/ssmv01/ccmd)
[![Build](https://img.shields.io/github/actions/workflow/status/SSMV01/ccmd/pylint.yml)](https://github.com/SSMV01/ccmd/actions)
[![Open Issues](https://img.shields.io/github/issues-raw/SSMV01/ccmd)](https://github.com/SSMV01/ccmd/issues)
[![License](https://img.shields.io/github/license/SSMV01/ccmd?color=blue)](https://github.com/SSMV01/ccmd/)


### customcmd (Under Development)
### Tested on
- Linux mint
- Arch Linux

## Requirements
- ### Linux based OS
- ### Python3
#### Note: Other OSes will be supported very soon.


# Installation

Download the source from [releases](https://github.com/ssmv01/ccmd/releases) and save it at /home/(user) as ccmd

Run the following in your terminal
```
cd ~/ccmd

rm -rf .git

sudo bash init.sh

ccmd --target default
```

You can replace *default* with the path to your preferred csv file

And you're all set!

# Usage

```
ccmd [command(s)] [option(s)...]
```

## Creating a New Custom Command
#### Note: If you create multiple commands with the same name they will all be executed when you run the command.

<br>

### Writing your command directly into the cmds.csv file
<br>

### Syntax

```
Actual Command,Command_name
```

USE `_` underscores for spaces in *command name*s

<br>

1: Open the csv file with:

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
**Write only one pair of command per row.**

USE `_` underscores for spaces in *Command names*

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
Actual Command: [Actual Command]
Command Name: [Command name]
```

Using `_` underscores here is not necessary

3: Press **Enter** to save

<br>

### Check Output and run commands


If output is equal to:

```
command ?= string || command , Command_Name
```

If output contains:

```
command ?: string || command , Command_name
```

### Explaination
- the first *command* is the command you want to initially run when you execute the custom command

- *?=* checks if the output of the first *command* is equal to string passed after *?=*

- *?:* checks if the output of the first *command* contains the string passed after *?:*

- After the *?= or ?:* give the string that you want to check in *or* compare with the output

- || executes the command given after it IF the condition is True

- Finally, write the command that you want to execute if the condition is true


<br>

## Using Your Commands
#### Note: All commands with the same name will be executed.

<br>

```
ccmd [Command Name]
```

### Using multiple commands

```
ccmd [command#1] [command#2] ...
```

<br>

### Using --output and --output-silent

*--output* = write to file and execute

```
ccmd [command(s)] --output [path to file]
```
You can replace *-o-utput* with *-o*

*--output-silent* = write to file

```
ccmd [command(s)] --output-silent [path to file]
```

You can replace *--output-silent* with *-oS*

<br>

## Opening the csv file

```
ccmd --opencsv
```

<br>

## Setting the location of the csv file

```
ccmd --target [Path to csv file]
```

If you don't have a specific csv file you want to use:

```
ccmd --target default
```

<br>

## Removing Commands

#### This feature will be added very soon.

For Now:

```
ccmd --opencsv
```

Find and Erase the row. (Try Ctrl + F)

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
cd ~/ccmd

bash uninstall.sh
```

Do not use _sudo_ here

---
<br>

### Info

_Version_: 0.2.8-alpha

_Author_: [SSMV01](https://github.com/SSMV01)

MIT License
