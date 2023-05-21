## Creating a new custom command

### Writing your commands directly into the commands.csv file
<br>

1: Open the csv file:

```
ccmd
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
command if= string run: command , Command_Name
```

If output contains:

```
command if: string run: command , Command_name
```

#### Explaination
- the first *command* is the command you want to initially run when you execute the custom command

- *if=* checks if the output of the first *command* is equal to string passed after *if=*

- *if:* checks if the output of the first *command* contains the string passed after *if:*

- After the *if= or if:* give the string that you want to check in *or* compare with the output

- run: executes the command given after it IF the condition is True

- Finally, write the command that you want to execute if the condition is true

### next> command

The `next>` command is used to separate two or more commands that are to be executed sequentially:

```
command#1 next> command#2 next> command#3 , command_name
```
