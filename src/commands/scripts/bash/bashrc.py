import os
from textwrap import dedent

def bashrc_setup(config, fpath):
    wspace = config.get('BASE', 'wspace')
    codespace = os.path.join(wspace, 'code')
    this_fpath = os.path.realpath(__file__)
    static_path = os.path.normpath(os.path.join(this_fpath,
                                                '..',
                                                'static/bashrc.txt'))

    with open(static_path, 'r') as brc:
        bashrc_additions = brc.read().replace('<workspace/code>', codespace)

    with open(fpath, 'a') as f:
        f.write(dedent(bashrc_additions))
    print(fpath)
    print("\nBashrc has been set up.\n")

    return
