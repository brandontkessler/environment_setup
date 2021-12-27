import os
import sys

def workspace_path(config):
    setup_path = config.get('BASE', 'workspacePath')

    if setup_path.casefold() == '~': 
        basedir = os.path.expanduser('~')
    elif os.path.exists(setup_path):
        basedir = setup_path
    elif '~' in setup_path:
        basedir = os.path.join(os.path.expanduser('~'), os.path.relpath(setup_path, '~'))
    else:
        print("\nExiting...\n")
        print(f"Unable to find path: '{setup_path}'.")
        print(f"Test this by running `ls {setup_path}` in the command line.")
        sys.exit("Please provide a path or use root directory.")

    wspace = os.path.join(basedir, 'Workspace')
    
    print(f"\nSetting up 'Workspace' in path: {wspace}\n")
    return wspace