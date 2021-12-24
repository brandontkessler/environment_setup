import os
from textwrap import dedent

def bash_setup(envdir):
    bash_input = input("Do you want to set up bash?\n[y/N]\n")

    if bash_input.casefold() != 'y':
        print("\nSkipping bash setup.\n")
        return
    
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

    bash_profile_additions = """
        if [ -f ~/.bashrc ]; then
            source ~/.bashrc
        fi
    """

    bash_prompt = r"""
        blue=$(tput setaf 33);
        yellow=$(tput setaf 11);
        red=$(tput setaf 124);
        green=$(tput setaf 64);
        white=$(tput setaf 7);
        bold=$(tput bold);
        reset=$(tput sgr0);

        PS1="\[${blue}\]\u";
        PS1+="\[${white}\]@";
        PS1+="\[${yellow}\]\h";
        PS1+="\[${white}\]: ";
        PS1+="\[${green}\]\w";
        PS1+="\n";
        PS1+="\[${white}\]$ \[${reset}\]";

        export PS1;
    """

    bash_aliases = f"""
        # Set Python
        alias python=python3

        # Easier navigation: .., ...
        alias ..="cd .."
        alias ...="cd ../.."
        alias toenv="cd {envdir}"
    """

    weather_path = os.path.join(envdir, 'code', 'daily_weather')
    bash_functions = fr"""
        function test_function() {{
            echo "Some test foo!"
            echo "Another line"
        }}

        function weather() {{
            source {weather_path}/venv/bin/activate
            python weather.py
            deactivate
        }}
    """

    with open(os.path.join(basedir, '.bashrc'), 'a') as f:
        f.write(dedent(bashrc_additions))
        f.write(dedent(pythonpath))

    with open(os.path.join(basedir, '.bash_profile'), 'a') as f:
        f.write(dedent(bash_profile_additions))
    
    with open(os.path.join(basedir, '.bash_prompt'), 'w') as f:
        f.write(dedent(bash_prompt))

    with open(os.path.join(basedir, '.bash_aliases'), 'a') as f:
        f.write(dedent(bash_aliases))

    with open(os.path.join(basedir, '.bash_functions'), 'a') as f:
        f.write(dedent(bash_functions))

    print("\nBash profiles have been set up.\n")

    return
