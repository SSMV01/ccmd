#!/usr/bin/python3
import os
import sys
import logging

USERNAME = os.environ.get('LOGNAME')

try:
    os.chdir(f'/home/{USERNAME}')
    os.makedirs('ccmd_tmp_folder')

    # Copy necessary files
    os.system('cp .ccmd/get_ccmd.py ./ccmd_tmp_folder')
    os.system('cp .ccmd/bin/cmds.csv ./ccmd_tmp_folder')
    os.system('cp .ccmd/bin/cmds_target.txt ./ccmd_tmp_folder')

    # Remove folder
    os.system('rm -rf .ccmd')

    # Reinstall ccmd
    os.system(f'{sys.executable} ccmd_tmp_folder/get_ccmd.py')

    # Replace necessary files
    os.system('rm -rf .ccmd/bin/cmds.csv')
    os.system('rm -rf .ccmd/bin/cmds_target.txt')
    os.system('cp ccmd_tmp_folder/cmds.csv .ccmd/bin')
    os.system('cp ccmd_tmp_folder/cmds_target.txt .ccmd/bin')

    # Remove tmp folder
    os.system('rm -rf ccmd_tmp_folder')

except KeyboardInterrupt:
    print()
    logging.info("Exiting...")
    sys.exit(1)
