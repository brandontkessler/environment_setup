import os
import json

from scripts.environment_path import environment_path
from scripts.folder_structure import folder_structure
from scripts.env_config_setup import env_config_setup
from scripts.git_repos import git_repos
from scripts.clear_env import clear_env
from scripts.bash_setup import bash_setup
from scripts.vscode_workspace import vscode_workspace
from scripts.aws_creds_setup import aws_creds_setup
from scripts.ssh_setup import ssh_setup


# Path and Configuration
envdir = environment_path()

env_config = {'envdir': envdir}

if os.path.exists('env_config.json'):
    print("Environment config file already exists and must be eliminated.")
    clear_env()

with open('env_config.json', 'w') as env_json:
    json.dump(env_config, env_json)

# Folders, environments and repos
folder_structure(envdir)
env_config_setup(envdir)
git_repos(envdir)

# Credentials Setup
os.system(f"touch {os.path.join(envdir, 'code', 'bcreds.json')}")
os.system(f"touch {os.path.join(envdir, 'work', 'code', 'bcreds.json')}")
aws_creds_setup()
ssh_setup()

# Bash Setup [optional]
bash_setup(envdir)

# 3rd Party Setups
vscode_workspace(envdir)
