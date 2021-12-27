import os
from textwrap import dedent

def bash_profile():
    basedir = os.path.expanduser('~')
    
    bash_profile_additions = """
        if [ -f ~/.bashrc ]; then
            source ~/.bashrc
        fi
    """

    with open(os.path.join(basedir, '.bash_profile'), 'a') as f:
        f.write(dedent(bash_profile_additions))

    print("\nBash profile has been set up.\n")

    return
