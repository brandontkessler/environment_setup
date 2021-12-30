import os
from textwrap import dedent

def bash_aliases(fpath):
    this_fpath = os.path.realpath(__file__)
    static_fpath = os.path.normpath(os.path.join(this_fpath, 
                                                 '..', 
                                                 'static/bash_aliases.txt'))

    with open(static_fpath, 'r') as ba:
        bash_aliases = ba.read()

    with open(fpath, 'a') as f:
        f.write(dedent(bash_aliases))

    print("\nBash aliases have been set up.\n")

    return
