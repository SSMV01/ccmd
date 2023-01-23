## CCMD
### customcmd

### This program is under development and has not been tested completely.
### Only works on linux

## Requirements

<ul>
<li><h3>python3</h3></li>
</ul>

# Installation
<p>1. Download the source code from <a href='https://github.com/SSMV01/ccmd/releases'>releases</a> and save it at the <i>/home/(user)/</i> directory as <i>ccmd</i>:</p>
<p>Saving the folder as 'ccmd' is a necessity.</p>
<p>Saving the ccmd folder at <i>/home/(user)/</i> is a necessity.</p>

<p>2. <code>cd</code> into the <i>ccmd</i> directory:</p>

```
cd ccmd
```

<p>3. Run the <i>init.sh</i> file with <code>bash</code>:</p>

```
sudo bash init.sh
```

<p><code>sudo</code> is necessary to access the '/bin' folder</p>

<p>4. Set your target file (csv file)'s path.</p>
<p>See: <a href='https://github.com/SSMV01/ccmd/#setting-the-location-of-the-csv-file'>Setting the location of the csv file</a></p>

<p>And you're all set!</p>

# Usage

<p><b>Basic Usage:</b></p>

```
ccmd <command(s)> <option(s)...>
```

## Creating a New Custom Command

<br>

### Note: If you create multiple commands with the same name they will all be executed when you run the command.

<br>

### <u>Writing your command directly into the cmds.csv file</u>
<br>

---

### Syntax

```
Actual Command,Your_command_name
```

<p>USE <code>_(s)</code> underscores for spaces ONLY for <i>Your command</i>s</p>
<p> Do not use spaces after the <i>Actual Command</i>.</p>

---

<br>

<br>
<p>1. Open the <b>cmds.csv</b> file located in the <i>ccmd/bin</i> folder</p>

See: [Opening the cmds.csv file from the terminal](https://github.com/SSMV01/CCMD#opening-the-cmdscsv-file-from-the-terminal)

<p>2. Write the Actual Commands first, then Your command seperated by a comma.<p>
<p>USE <code>_(s)</code> underscores for spaces ONLY FOR 'YOUR COMMAND NAMES'</p>
<p><b>Write only one pair of command per row.</b></p>

```
Actual Command-1,Your_Command_name-1
Actual Command-2,Your_Command_name-2
...
...
```

<p>3. Save and close the file once you are done.</p>

<br>

### <u>Creating commands from terminal</u>
<br>
<p>1. Use <b>-new</b>:</p>

```
ccmd -new
```

<p>2. Enter the values for the inputs:</p>

```
Actual Command: <Command To Replace>
Replacement Command: <Your Command name>
```

<p>You dont have to use <code>_(s)</code> underscores for spaces here in <i>Replacement Command</i></p>

<p>3. Press <b>Enter</b> to save.</p>

### <u>Check Output and run commands</u>
<p>Write these commands in the <i>cmds.csv</i> file or when you run <i>-new</i></p>
<p>You can only use this feature in the <i>Actual commands</i> part</p>
<p>Syntax:</p>

<p>If output is equal to:</p>

```
Actual Command ?= string to compare with output || command to run if output equals the given string,Your_Command_name
```

<p>If output contains:</p>

```
Actual Command ?: string to check in output || command to run if output contains the given string,Your_Command_name
```

<h3>Explaination</h3>
<p>- <i>Actual Command</i> is the command you want to initially run when you execute the custom command</p>
<p>- <i>?=</i> checks if the output of the <i>Actual Command</i> is equal to string passed after <i>?=</i></p>
<p>- <i>?:</i> checks if the output of the <i>Actual Command</i> contains the string passed after <i>?:</i></p>
<p>- After the <i>?= or ?:</i> give the string that you want to check in <i>or</i> compare with the output</p>
<p>- || executes the command given after it IF the condition is TRUE</p>
<p>- Finally, write the command that you want to execute if the condition is true</p>


<br>

## Opening the cmds.csv file from the terminal

<p>We recommend you to use a text editor to open the csv file instead of excel like software.</p>

```
ccmd --opencsv
```

## Setting the location of the csv file

```
ccmd --target <Path to csv file>
```

If you don't have a specific csv file you want to use:

```
ccmd --target default
```

## Using Your Commands

<br>

### Note: If you have multiple commands with the same name they will all be executed when you run the command.

<br>

<p>Note: Its not necessary to use <code>_(s)</code> underscores for spaces here but you can do so to avoid the usage of <code>""</code><p>

```
ccmd <Your Command>
```
<p><b>If your command contains space use double quotes or <code>_(s)</code>underscores:</b></p>

```
ccmd "<Your Command>"
```
OR

```
ccmd Your_Command
```
### <u>Using multiple commands</u>
<br>

```
ccmd <command 1> <command 2> ...
```

### <u>Using -o and -oS</u>
<br>

<p> <i>-o</i> writes the output(s) to the specified file <b>AND</b> also runs the command in your terminal.

```
ccmd <command(s)> -o <out_file>
```

<p> <i>-oS</i> writes the output(s) to the specified file but <b>DOES NOT</b> run the command in your terminal.

```
ccmd <command(s)> -oS <out_file>
```

## Removing Commands
<br>

<p>1. Open the <i>cmds.csv</i> file</p>

```
ccmd --opencsv
```

<p>2. Find and Erase the row.</p>

## Uninstallation

<p>Run the <i>uninstall.sh</i> file location the ccmd directory</p>

```
bash uninstall.sh
```

<p>Do not use <i>sudo</i> here</p>

---
<br>

### Info
<p><i>Version</i>: 0.1.1</p>
<p><i>Author</i>: <a href="https://github.com/SSMV01">SSMV01</a></p>
<p>MIT License</p>
