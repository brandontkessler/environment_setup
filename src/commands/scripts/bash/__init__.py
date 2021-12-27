from .bashrc import bashrc_setup
from .bash_profile import bash_profile
from .bash_aliases import bash_aliases
from .bash_prompt import bash_prompt
from .bash_functions import bash_functions

def bash_setup(config):
    if config.getboolean('BASH', 'setupBash', fallback=False) is True:
        bashrc_setup(config)
        bash_profile()
        bash_aliases(config)
        bash_prompt()
        bash_functions(config)
    else:
        print("\nSkipping bash setup\n")