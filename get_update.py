#!/usr/bin/python3
import os
import sys
import logging
import subprocess

USERNAME = os.environ.get('LOGNAME')

try:
    os.chdir(f'/home/{USERNAME}')
    os.makedirs('ccmd_tmp_folder')

    # Copy necessary files
    subprocess.check_call(['cp', '.ccmd/get_ccmd.py', './ccmd_tmp_folder'], shell=False)
    subprocess.check_call(['cp', '.ccmd/bin/cmds.csv', './ccmd_tmp_folder'], shell=False)
    subprocess.check_call(['cp', '.ccmd/bin/cmds_target.txt', './ccmd_tmp_folder'], shell=False)

    # Remove folder
    subprocess.check_call(['rm', '-rf', '.ccmd'], shell=False)

    # Reinstall ccmd
    subprocess.check_call([sys.executable, 'ccmd_tmp_folder/get_ccmd.py'], shell=False)

    # Replace necessary files
    subprocess.check_call(['rm', '-rf', '.ccmd/bin/cmds.csv'], shell=False)
    subprocess.check_call(['rm', '-rf', '.ccmd/bin/cmds_target.txt'], shell=False)
    subprocess.check_call(['cp', 'ccmd_tmp_folder/cmds.csv', '.ccmd/bin'], shell=False)
    subprocess.check_call(['cp', 'ccmd_tmp_folder/cmds_target.txt', '.ccmd/bin'], shell=False)

except subprocess.CalledProcessError as e:
    print(e)
    sys.exit(2)

except KeyboardInterrupt:
    print()
    logging.info("Exiting...")
    sys.exit(1)

finally:
    # Remove tmp folder
    subprocess.check_call(['rm', '-rf', 'ccmd_tmp_folder'])
