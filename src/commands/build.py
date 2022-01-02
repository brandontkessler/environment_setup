import os

from .scripts import setup, git, creds, ssh, bash, third_party_apps as thrdp
from .helpers import config as config_helper


def build(mode='prod'):
    if mode == 'prod':
        config = config_helper.read_config('config.ini')
        wspace = setup.workspace_path(config, mode)
        config['BASE']['wspace'] = wspace

        # store updated configs to use for teardown
        with open('.workspace_config.ini', 'w') as f:
            config.write(f)

        # reset the config template
        shutil.copy(os.path.join('templates', 'config_template.ini'), 'config.ini')
    
    elif mode == 'test':
        config = config_helper.read_config('templates/test_config_template.ini')
        wspace = setup.workspace_path(config, mode)
        config['BASE']['wspace'] = wspace

    else:
        raise Exception('Incorrect mode selected')


    # Folder setup
    setup.folder_structure(config)

    # Git Setup
    git.repo_setup(config)
    git.git_config(config)

    # Credentials Setup
    creds.setup_bcreds(config)
    creds.aws_creds_setup(config)

    # SSH Setup
    ssh.ssh_config(config)
    ssh.keygen(config)

    # Bash Setup
    bash.bash_setup(config)

    # 3rd Party Setups
    thrdp.vscode_workspace(config)

if __name__=='__main__':
    build('test')