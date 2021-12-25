import os

def repo_setup(config):    
    repos = config.get('GIT', 'repos')
    envdir = config.get('BASE', 'envdir')
    
    for repo_config in repos.split('\n')[1:]:
        
        repo_url = repo_config.split(' ')[0] # flags come after the first space
        repo = repo_url.split('/')[-1].replace('.git', '')

        path = f'{envdir}/notes/' if repo == 'notes' else f'{envdir}/code/{repo}/'

        gitcmd = f"git clone {repo_url} {path}"

        os.system(gitcmd)

        if ' -v' in repo_config:
            activate_env = f'source {envdir}/code/{repo}/venv/bin/activate'
            pips = f'pip install --upgrade pip && pip install -r {envdir}/code/{repo}/requirements.txt'

            os.system(f'python3 -m venv {envdir}/code/{repo}/venv')
            os.system(f'{activate_env} && {pips} && deactivate')

    print("\nAll repos have been cloned.\n")

    return
