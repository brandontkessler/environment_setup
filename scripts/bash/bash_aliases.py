import os
from textwrap import dedent

def bash_aliases(config):
    envdir = config.get('BASE', 'envdir')
    basedir = os.path.expanduser('~')
    
    bash_aliases = f"""
        # Set Python
        alias python=python3

        # Easier navigation: .., ...
        alias ..="cd .."
        alias ...="cd ../.."
        alias toenv="cd {envdir}"
    """

    with open(os.path.join(basedir, '.bash_aliases'), 'a') as f:
        f.write(dedent(bash_aliases))

    print("\nBash aliases have been set up.\n")

    return
