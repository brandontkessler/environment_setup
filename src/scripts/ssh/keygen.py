import os

def keygen(config):
    ssh_path = os.path.join(os.path.expanduser('~'), '.ssh')

    genkeys = config.getboolean('SSH', 'genKeys', fallback=False)
    keyname = config.get('SSH', 'keyName', fallback='idrsa')

    if genkeys is True:
        os.system(f"ssh-keygen -t rsa -b 4096 -f {os.path.join(ssh_path, keyname)}")
    else:
        print('\nSkipping keygen...\n')

    return