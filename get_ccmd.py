import os
import sys
import logging
import subprocess
from os import chdir, environ
from subprocess import check_call, Popen, PIPE

logging.basicConfig(format="%(levelname)s: %(message)s")
logging.getLogger().setLevel(logging.INFO)

USERNAME = environ.get('LOGNAME')
VERSION = "v0.4.4-alpha"

print("CCMD")
print('-' * 20)
print("Starting installation...")
print("DO NOT USE KeyboardInterrupt\n")

chdir(f'/home/{USERNAME}')


def install_dependencies():
    logging.info("Installing dependencies...")
    try:
        with Popen([sys.executable, '-m', 'pip', 'install', 'colorama'], stdout=PIPE, stderr=PIPE,
                   start_new_session=True) as install_colorama:
            if b"No module named pip" in install_colorama.stderr.read():
                logging.error("pip not installed")
                sys.exit(2)

            elif install_colorama.stderr.read() != b'':
                print(install_colorama.stderr.read())

            else:
                logging.info("Done.")

    except KeyboardInterrupt:
        print()
        logging.info("Exiting...")
        sys.exit(1)


def clone():
    logging.info("Cloning ccmd...")
    try:
        with Popen(['git', 'clone', 'https://github.com/ssmv01/ccmd', f'/home/{USERNAME}/.ccmd'], stdout=PIPE, stderr=PIPE,
                   start_new_session=True) as clone_ccmd:
            if b"Could not resolve host: github.com" in clone_ccmd.stderr.read():
                logging.error("Failed to access github.com")
            else:
                logging.info("Done.")

    except FileNotFoundError as exception:
        print(exception)
        sys.exit(2)

    except KeyboardInterrupt:
        print()
        logging.info("Exiting...")
        sys.exit(1)


def setup_file():
    chdir(f'/home/{USERNAME}/.ccmd')
    logging.info("Setting up files...")

    try:
        check_call(['/usr/bin/chmod', '+x', 'data/ccmd.sh'], shell=False)
        check_call(['/usr/bin/cp', 'data/ccmd.sh', f'/home/{USERNAME}/.local/bin/ccmd'], shell=False)
        SHELL = os.getenv('SHELL')
        SHELL = SHELL.split("/")[-1]
        with open(f'/home/{USERNAME}/.{SHELL}rc', 'a', encoding='utf-8') as rc:
            rc.write("\n#CCMD")
            rc.write("\nexport PATH=$PATH:/home/ssmv/.local/bin")
        logging.info("Done.")

    except subprocess.CalledProcessError as exception:
        print(exception)
        sys.exit(2)


def setup():
    logging.info("Clearing things up...")
    chdir(f'/home/{USERNAME}/.ccmd')

    try:
        check_call(['/usr/bin/rm', '-rf', '.git'], shell=False)
        check_call(['/usr/bin/rm', '-rf', '.github'], shell=False)
        check_call(['/usr/bin/rm', '.gitignore'], shell=False)
        check_call([f'/home/{USERNAME}/.local/bin/ccmd', '--setcsv', 'default'], shell=False)
        setup_file()

    except subprocess.CalledProcessError as exception:
        print(exception)
        sys.exit(2)

    logging.info("Installation complete.")


def main():
    try:
        if os.path.exists(f'/home/{USERNAME}/.ccmd'):
            if os.path.exists(f'/home/{USERNAME}/.local/bin/ccmd'):
                print(f"\nMake sure '/home/{USERNAME}/.local/bin' is in PATH")
                logging.info("CCMD is already installed")
                sys.exit(0)
            else:
                setup_file()
        else:
            install_dependencies()
            clone()
            setup_file()
            setup()
            print(f'\n{VERSION}')

    except KeyboardInterrupt:
        print()
        logging.info("Exiting...")
        sys.exit(1)


if __name__ == '__main__':
    main()
