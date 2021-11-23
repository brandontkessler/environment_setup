import os

def git_repos(envdir):
    repos = [
        'notes',
        'GenData',
        'decorators',
        'data_structures'
    ]

    for repo in repos:
        path = f'{envdir}/notes/' if repo == 'notes' else f'{envdir}/code/{repo}/'
        gitcmd = f"git clone https://github.com/brandontkessler/{repo}.git {path}"

        os.system(gitcmd)

    print("\nAll repos have been cloned.\n")
    return
