#!/usr/bin/bash

if rm ~/.local/bin/ccmd && rm -r ~/.ccmd; then
    echo Sucessfully uninstalled.
else
    echo uninstallation failed!
fi