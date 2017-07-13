import os
import stat
import sys
import subprocess

from marina.package_utils import get_venv_basedir


def download_sugarcli(install_path: str):
    from urllib.request import urlretrieve
    # download sugarcli if it's not the case
    if os.path.isfile(install_path) is False:
        print('sugarcli has not been downloaded yet, downloading ...')
        urlretrieve('http://apt.inetprocess.fr/pub/sugarcli', install_path)
        os.chmod(install_path, stat.S_IRWXU)


def run(vm_name: str, relative_dir: str, sugarcli_cmd: str):
    home = get_venv_basedir() + '/home/www-data'
    if os.path.isdir(home) and not os.path.isdir(home + '/bin'):
        os.mkdir(home + '/bin')

    download_sugarcli(home + '/bin/sugarcli')

    tty = 't' if sys.stdin.isatty() else ''
    cmd = ['docker', 'exec', '-u', 'www-data', '-i' + tty, vm_name]
    cmd += ['bash', '-c', '--']
    cmd += ['cd /var/' + relative_dir + '; exec /usr/bin/php ~/bin/sugarcli {}'.format(sugarcli_cmd)]
    subprocess.call(cmd, stdin=sys.stdin, stderr=subprocess.STDOUT)
