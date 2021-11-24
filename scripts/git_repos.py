import os

def git_repos(envdir):
    repos = [
        'notes',
        'GenData',
        'decorators',
        'data_structures',
        'daily_weather'
    ]

    for repo in repos:
        path = f'{envdir}/notes/' if repo == 'notes' else f'{envdir}/code/{repo}/'
        gitcmd = f"git clone https://github.com/brandontkessler/{repo}.git {path}"

        os.system(gitcmd)

        ## Create environments and install requirements
        if repo in ('daily_weather'):
            os.system(f'python -m venv {envdir}/code/{repo}/venv')
            os.system(f'source {envdir}/code/{repo}/venv/bin/activate')
            os.system(f'pip install --upgrade pip && pip install -r requirements.txt')
            os.system('deactivate')

    print("\nAll repos have been cloned.\n")

    return
