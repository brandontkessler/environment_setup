import os
from configparser import ConfigParser

import scripts.base as base
import scripts.git_setup as git
import scripts.credential_setup as cred_setup
import scripts.ssh as ssh
import scripts.bash as bash
import scripts.third_party_apps as thrdp


# Get Configs
config = ConfigParser()
config.read('config.ini')
testing = config.getboolean('TEST', 'active')

# Pathing Setup
if testing:
    envdir = os.path.join(os.path.expanduser('~'), config.get('TEST', 'path'))
else: 
    envdir = base.environment_path(config)

# Add envdir to config file
config['BASE']['envdir'] = envdir

with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Folder setup
base.folder_structure(config)

# Git Setup
# git.git_repos(config)
git.git_config(config)

# Credentials Setup
cred_setup.setup_bcreds(config)
cred_setup.aws_creds_setup(config)

# SSH Setup
ssh.ssh_config()
ssh.keygen(config)

# Bash Setup
bash.bash_setup(config)

# 3rd Party Setups
thrdp.vscode_workspace(config)
