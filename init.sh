#!/usr/bin/bash

if chmod +x bin/ccmd.sh && cp bin/ccmd.sh ~/.local/bin/ccmd && pip install colorama; then
    echo Sucessfully initialized.
else
    echo initialization failed!
fi