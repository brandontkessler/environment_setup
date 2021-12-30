import os

from .bashrc import bashrc_setup
from .bash_profile import bash_profile
from .bash_aliases import bash_aliases
from .bash_prompt import bash_prompt
from .bash_functions import bash_functions

def bash_setup(config, rootdir = os.path.expanduser('~')):
    if config.getboolean('BASH', 'setupBash', fallback=False) is True:
        bashrc_setup(config, os.path.join(rootdir, '.bashrc'))
        bash_profile(os.path.join(rootdir, '.bash_profile'))
        bash_aliases(os.path.join(rootdir, '.bash_aliases'))
        bash_prompt(os.path.join(rootdir, '.bash_prompt'))
        bash_functions(config, os.path.join(rootdir, '.bash_functions'))
    else:
        print("\nSkipping bash setup\n")