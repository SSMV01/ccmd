#!/usr/bin/bash

if chmod +x bin/ccmd.sh && cp bin/ccmd.sh ~/.local/bin/ccmd; then
    if pip install colorama; then  
        echo Sucessfully initialized.
    else
        echo Make sure pip is installed
    fi
else
    echo initialization failed!
fi
