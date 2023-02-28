import os
import sys
import logging
import subprocess
from os import chdir, environ
from subprocess import check_call, Popen, PIPE
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

USERNAME = environ.get('LOGNAME')

print("CCMD")
print('-' * 20)
print("Starting installation")

chdir(f'/home/{USERNAME}')

retry = 0

def install_dependencies():
    logging.info("Installing dependencies...")
    with Popen([sys.executable, '-m', 'pip', 'install', 'colorama'], stdout=PIPE, stderr=PIPE) as install_colorama:
        if b"No module named pip" in install_colorama.stderr.read():
            logging.error("pip not installed")
            sys.exit(2)

        elif install_colorama.stderr.read() != b'':
            print(install_colorama.stderr.read())

        else:
            logging.info("Done.")

def clone():
    logging.info("Cloning ccmd...")
    try:
        with Popen(['git', 'clone', 'https://github.com/ssmv01/ccmd'], stdout=PIPE, stderr=PIPE) as clone_ccmd:
            if b"Could not resolve host: github.com" in clone_ccmd.stderr.read():
                logging.error("Failed to access github.com")
            else:
                logging.info("Done.")

    except FileNotFoundError as exception:
        print(exception)
        sys.exit(2)

def rename():
    check_call('mv ccmd .ccmd', shell=True)

def setup():
    logging.info("Setting things up...")
    chdir(f'/home/{USERNAME}/.ccmd')

    try:
        check_call('rm -rf .git', shell=True)
        check_call('rm -rf .github', shell=True)
        check_call('rm .gitignore', shell=True)
        setup_file()

    except subprocess.CalledProcessError as exception:
        print(exception)
        sys.exit(2)

    print()
    logging.info("Installation complete")
    print(f"**Add '/home/{USERNAME}/.local/bin' to your PATH variable**\n")

def setup_file():
    chdir(f'/home/{USERNAME}/.ccmd')
    logging.info("Setting up the file...")

    try:
        check_call('chmod +x bin/ccmd.sh', shell=True)
        check_call('cp bin/ccmd.sh ~/.local/bin/ccmd', shell=True)
        logging.info("Done.")

    except subprocess.CalledProcessError as exception:
        print(exception)
        sys.exit(2)

def main():
    if os.path.exists(f'/home/{USERNAME}/.ccmd'):
        if os.path.exists(f'/home/{USERNAME}/.local/bin/ccmd'):
            logging.info("CCMD is already installed")
            sys.exit(0)
        else:
            setup_file()
    else:
        install_dependencies()
        clone()
        rename()
        setup()

if __name__ == '__main__':
    main()
