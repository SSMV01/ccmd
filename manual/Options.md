<details>
    <summary>Table of contents</summary>
    <ol>
        <li><a href="#opening-the-csv-file">Opening the csv file</a></li>
        <li><a href="#list-commands">List commands</a></li>
        <li><a href="#remoing-commands">Removing commands</a></li>
        <li><a href="#display-version">Display version</a></li>
        <li><a href="#updating">Updating</a></li>
        <li><a href="#uninstalling">Uninstalling</a></li>
    </ol>
</details>

## Opening the csv file

Executing ccmd without any arguments will open the csv file:

```
ccmd
```

<br>

## Setting the location of the csv file

```
ccmd --setcsv <absolute_path_to_csv_file>
```

If you don't have a specific csv file you want to use:

```
ccmd --setcsv default
```

<br>

## List commands

If the command name is highlighted in Blue then it is a [check-if](https://github.com/ssmv01/ccmd#check-if-commands) command.

```
ccmd --list
```

OR

```
ccmd -l
```

## Removing commands

#### This feature will be added very soon.

For Now:

```
ccmd
```

Find and Erase the row. (Try `Ctrl + F if` you are using a graphical editor)

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

## Updating

Use the `--update` option to get the latest changes made to the repo:

```
ccmd --update
```

## Uninstalling

Use the `--uninstall` option:

```
ccmd --uninstall
```
