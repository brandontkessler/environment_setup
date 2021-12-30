import os
from textwrap import dedent

def bash_prompt(fpath):
    this_fpath = os.path.realpath(__file__)
    static_path = os.path.normpath(os.path.join(this_fpath,
                                                '..',
                                                'static/bash_prompt.txt'))

    with open(static_path, 'r') as bp:
        bash_prompt = bp.read()

    with open(fpath, 'w') as f:
        f.write(dedent(bash_prompt))

    print("\nBash prompt has been set up.\n")

    return
