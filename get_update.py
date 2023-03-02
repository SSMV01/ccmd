#!/usr/bin/python3

import os
import sys

USERNAME = os.environ.get('LOGNAME')

os.chdir(f'/home/{USERNAME}')
os.makedirs('ccmd_tmp_folder')
os.system('cp .ccmd/get_ccmd.py ./ccmd_tmp_folder')
os.system('rm -rf .ccmd')
os.chdir(f'/home/{USERNAME}/ccmd_tmp_folder')
os.system(f'{sys.executable} get_ccmd.py')
os.chdir(f'/home/{USERNAME}')
os.system('rm -rf ccmd_tmp_folder')