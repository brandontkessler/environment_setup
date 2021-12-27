import os

def repo_setup(config):
    if config.getboolean('GIT', 'setupGitRepos') is True:
        repos = config.get('GIT', 'repos')
        wspace = config.get('BASE', 'wspace')
        
        for repo_config in repos.split('\n')[1:]:
            
            repo_url = repo_config.split(' ')[0] # flags come after the first space
            repo = repo_url.split('/')[-1].replace('.git', '')

            path = f'{wspace}/notes/' if repo == 'notes' else f'{wspace}/code/{repo}/'

            gitcmd = f"git clone {repo_url} {path}"

            os.system(gitcmd)

            if ' -v' in repo_config:
                activate_env = f'source {wspace}/code/{repo}/venv/bin/activate'
                pips = f'pip install --upgrade pip && pip install -r {wspace}/code/{repo}/requirements.txt'

                os.system(f'python3 -m venv {wspace}/code/{repo}/venv')
                os.system(f'{activate_env} && {pips} && deactivate')

        print("\nAll repos have been cloned.\n")
    else:
        print("\nSkipping repo setup\n")

    return
