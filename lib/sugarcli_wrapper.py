import os
import stat
import sys
import subprocess


def download_sugarcli(install_path: str):
    from urllib.request import urlretrieve
    # download sugarcli if it's not the case
    if os.path.isfile(install_path) is False:
        urlretrieve('http://apt.inetprocess.fr/pub/sugarcli.phar', install_path)
        os.chmod(install_path, stat.S_IRWXU)
        print('sugarcli has not been downloaded yet, downloading ...')


def run(vm_name: str, relative_dir: str, sugarcli_cmd: str):
    download_sugarcli('home/www-data/bin/sugarcli.phar')

    tty = 't' if sys.stdin.isatty() else ''
    cmd = ['docker', 'exec', '-u', 'www-data', '-i' + tty, vm_name]
    cmd += ['bash', '-c', '--']
    cmd += ['cd /var/' + relative_dir + '; exec /usr/bin/php ~/bin/sugarcli.phar {}'.format(sugarcli_cmd)]
    subprocess.call(cmd, stdin=sys.stdin, stderr=subprocess.STDOUT)
