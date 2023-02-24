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
        elif install_colorama.stderr:
            print(install_colorama.stderr.read())
        else:
            with Popen(['echo', '$PATH'], stdout=PIPE) as verify_path:
                if b'/home/{USERNAME}/.local/bin' not in verify_path.stdout.read():
                    check_call(f'export PATH=/home/{USERNAME}/.local/bin:$PATH')
            logging.info("Done.")

logging.info("Installing dependencies...")
install_dependencies()

logging.info("Cloning ccmd...")
try:
    with Popen(['git', 'clone', 'https://github.com/ssmv01/ccmd'], stdout=PIPE, stderr=PIPE) as clone_ccmd:
        if "Could not resolve host: github.com" in clone_ccmd.stderr.read():
            logging.error("Failed to access github.com")
        else:
            logging.info("Done.")

except FileNotFoundError as exception:
    print(exception)

check_call('mv ccmd .ccmd', shell=True)

chdir(f'/home/{USERNAME}/.ccmd')

check_call('chmod +x bin/ccmd.sh', shell=True)
check_call('cp bin/ccmd.sh ~/.local/bin/ccmd', shell=True)

logging.info("Installation complete\n")

check_call('ccmd', shell=True)
