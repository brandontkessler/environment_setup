import os
from textwrap import dedent

def bash_functions(config, fpath):
    wspace = config.get('BASE', 'wspace')
    basedir = os.path.expanduser('~')
    this_fpath = os.path.realpath(__file__)
    static_path = os.path.normpath(os.path.join(this_fpath,
                                                '..',
                                                'static/bash_functions.txt'))

    weather_path = os.path.join(wspace, 'code', 'daily_weather')

    with open(static_path, 'r') as bf:
        bash_functions = bf.read().replace('<weather_path>', weather_path)

    with open(fpath, 'a') as f:
        f.write(dedent(bash_functions))

    print("\nBash functions have been set up.\n")

    return

