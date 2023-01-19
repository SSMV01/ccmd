# CustomCmd

### <u>Please use this software for ethical purposes only</u>

### NOTE: This application only supports linux and has only been tested on [Kali Linux](https://www.kali.org/)

# Installation
<p>1. Run the following command in the directory you want to install <b>CustomCmd</b>:</p>

```
git clone https://github.com/SSMV01/CustomCmd
```

<p>2. <code>cd</code> into the <i>CustomCmd</i> directory:</p>

```
cd CustomCmd
```

<p>3. Run the <i>init.sh</i> file with <code>bash</code>:</p>

```
sudo bash init.sh
```

<p>Note: <code>sudo</code> is necessary to access the '/bin' folder</p>

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

<p> Note: You dont have to use <code>_(s)</code> for spaces here in <i>Replacement Command</i></p>

<p>3. Press <b>Enter</b> to save.</p>

### <u>Writing your command directly into the cmds.csv file</u>
<br>

---

### Syntax

```
Acutal Command,Your_command_name
```

<p>USE <code>_(s)</code> for spaces ONLY for <i>Your command</i>s</p>

---

<br>

See: [Opening the cmds.csv file from the terminal](https://github.com/SSMV01/CustomCmd#opening-the-cmdscsv-file-from-the-terminal)
<br>
<p>1. Open the <b>cmds.csv</b> file located in the <i>bin</i> folder</p>
<p>2. Write the Actual Commands first, then Your command seperated by a comma.<p>
<p>use <code>_(s)</code> for spaces <b>ONLY FOR 'YOUR COMMAND NAMES'</b></p>
<p><b>Write only one pair of command per row.</b></p>

```
Actual Command-1,Your_Command_name-1
Actual Command-2,Your_Command_name-2
...
...
```

<p>3. Save and close the file once you are done.</p>

### <u>Check Output and run commands</u>
<p>Write these commands in the <i>cmds.csv</i> file or when you run <i>-new</i></p>
<p>Note: You can only use this feature in the <i>Actual commands</i> part</p>
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

```
ccmd --opencsv
```

## Using Your Commands

<br>

### Note: If you have multiple commands with the same name they will all be executed when you run the command.

<br>

<p>Note: Its not necessary to use <code>_(s)</code> for spaces here but you can do so to avoid the usage of <code>""</code><p>

```
ccmd <Your Command>
```
<p><b>If your command contains space use double quotes:</b></p>

```
ccmd "<Your Command>"
```
### <u>Using multiple commands</u>
<br>

```
ccmd <Command 1> <Command 2> ...
```

### <u>Using -o and -oS</u>
<br>

<p> <i>-o</i> writes the output(s) to the specified file <b>AND</b> also runs the command in your terminal.

```
ccmd <Command(s)> -o <path to file>
```

<p> <i>-oS</i> writes the output(s) to the specified file but <b>DOES NOT</b> run the command in your terminal.

```
ccmd <Command(s)> -oS <path to file>
```

## Removing Commands
<br>

<p>1. Open the <i>cmds.csv</i> file</p>

```
ccmd --opencsv
```

<p>2. Find and Erase the row.</p>

---
<br>

### Info
<p><i>Version</i>: 0.8.11-Alpha</p>
<p><i>Author</i>: <a href="https://github.com/SSMV01">SSMV</a></p>
<p>Copyright © 2022 SSMV.</p>
