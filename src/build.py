import scripts.setup as setup
import scripts.git as git
import scripts.creds as creds
import scripts.ssh as ssh
import scripts.bash as bash
import scripts.third_party_apps as thrdp
import helpers as h


# Get Configs
config = h.read_config('config.ini')

wspace = setup.workspace_path(config)
config['BASE']['wspace'] = wspace

with open('.workspace_config.ini', 'w') as f:
    config.write(f)

h.reset_config_template()

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
