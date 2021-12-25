import os
from textwrap import dedent

def bashrc_setup(config):
    envdir = config.get('BASE', 'envdir')
    basedir = os.path.expanduser('~')
    
    pythonpath = f"""
        PYTHONPATH=$PYTHONPATH:{os.path.join(envdir, 'code')}
        export PYTHONPATH
    """

    bashrc_additions = """
        if [ -f ~/.bash_prompt ]; then
            . ~/.bash_prompt
        fi

        if [ -f ~/.bash_aliases ]; then
            . ~/.bash_aliases
        fi

        if [ -f ~/.bash_functions ]; then
            . ~/.bash_functions
        fi
    """

    with open(os.path.join(basedir, '.bashrc'), 'a') as f:
        f.write(dedent(bashrc_additions))
        f.write(dedent(pythonpath))
    
    print("\nBashrc has been set up.\n")

    return
