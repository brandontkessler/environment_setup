import os
from textwrap import dedent

def bash_prompt():
    basedir = os.path.expanduser('~')
    
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

    with open(os.path.join(basedir, '.bash_prompt'), 'w') as f:
        f.write(dedent(bash_prompt))

    print("\nBash prompt has been set up.\n")

    return
