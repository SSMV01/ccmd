## Creating a new custom command

### Writing your custom commands directly into the csv file
<br>

1: Open the csv file:

```
ccmd
```

2: Write the Actual Commands first, then the Command Name you want to use, seperated by a comma as shown below:


```
Actual Command#1 , Command_name#1
Actual Command#2 , Command_name#2
...
...
```
USE `_` underscores for spaces in *Command names*

**Create only one custom command per row.**


3: Save and close the file once you are done.

<br>

### Creating custom commands from terminal
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

### next>

The `next>` command is used to execute multiple commands sequentially:

```
command#1 next> command#2 next> command#3 , command_name
```

<br>

### Conditionals


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

- After *if= or if:* is the string that you want to check in *or* compare with the output

- *run:* executes the command written after it IF the condition is True

- Finally, write the command that you want to execute IF the condition is True
