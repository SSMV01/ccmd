import os
import sys
import subprocess

USERNAME = os.environ.get('LOGNAME')

print("CCMD")
print('-' * 20)
print("Starting installation")

os.chdir(f'/home/{USERNAME}')
subprocess.check_call('git clone https://github.com/ssmv01/ccmd', shell=True)
subprocess.check_call('mv ccmd .ccmd', shell=True)
os.chdir(f'/home/{USERNAME}/.ccmd')
subprocess.check_call('chmod +x bin/ccmd.sh', shell=True)
subprocess.check_call('cp bin/ccmd.sh ~/.local/bin/ccmd', shell=True)
subprocess.check_call(f'{sys.executable} -m pip install colorama', shell=True)

print("\nInstallation complete")

subprocess.check_call('ccmd', shell=True)
