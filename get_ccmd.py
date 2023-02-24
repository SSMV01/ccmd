import os
import sys
import logging
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
            if retry == 1:
                logging.error("Failed to install pip")
                logging.info("exiting...")
                sys.exit(2)

            logging.info("Installing pip...")
            with Popen([ sys.executable ,'-m', 'ensurepip', '--upgrade'], stdout=PIPE, stderr=PIPE) as install_pip:
                if install_pip.stderr.read() == None:
                    logging.info("pip installed.")
                    check_call(f'export PATH=/home/{USERNAME}/.local/bin:$PATH')
                    retry += 1
                    install_dependencies()
                else:
                    logging.error("Failed to install pip")
                    logging.info("exiting...")
                    sys.exit(2)
        elif install_colorama.stderr.read() != b'':
            print(install_colorama.stderr.read())
        else:
            with Popen(['echo', '$PATH'], stdout=PIPE) as verify_path:
                if b'/home/{USERNAME}/.local/bin' not in verify_path.stdout.read():
                    check_call(f'export PATH=/home/{USERNAME}/.local/bin:$PATH', shell=True)
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

def rename():
    check_call('mv ccmd .ccmd', shell=True)

def setup():
    logging.info("Setting things up...")
    chdir(f'/home/{USERNAME}/.ccmd')

    check_call('rm -rf .git', shell=True)
    check_call('rm -rf .github', shell=True)
    check_call('rm .gitignore', shell=True)
    check_call('chmod +x bin/ccmd.sh', shell=True)
    check_call('cp bin/ccmd.sh ~/.local/bin/ccmd', shell=True)
    
    print()
    check_call('ccmd --setcsv default', shell=True)
    check_call('ccmd', shell=True)

    print()
    logging.info("Installation complete\n")
    
def main():
    if os.path.exists(f'/home/{USERNAME}/.ccmd'):
        if os.path.exists(f'/home/{USERNAME}/.local/bin/ccmd'):
            logging.info("CCMD is already installed")
            sys.exit(0)
        else:
            setup()
    else:
        install_dependencies()
        clone()
        rename()
        setup()

if __name__ == '__main__':
    main()
