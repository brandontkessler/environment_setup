import os
from textwrap import dedent

def bash_profile(fpath):
    bash_profile_additions = """
        if [ -f ~/.bashrc ]; then
            source ~/.bashrc
        fi
    """

    with open(fpath, 'a') as f:
        f.write(dedent(bash_profile_additions))

    print("\nBash profile has been set up.\n")

    return
