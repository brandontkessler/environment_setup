import os
import sys
import shutil

def folder_structure(config):
    wspace = config.get('BASE', 'wspace')

    # Set up backups folder
    os.makedirs(os.path.join(os.path.expanduser('~'), 'backups'), exist_ok=True)

    if os.path.exists(wspace):
        msg = f"Workspace folder already exists in at path: {wspace}. Delete and rebuild?\n[y/N]\n"
        env_exists_response = input(msg)

        if env_exists_response.casefold() != 'y'.casefold(): 
            sys.exit("\nExiting...\nInput of 'y' needed to continue.")

        print("Clearing existing 'Workspace' folder in root directory.")
        shutil.rmtree(wspace)

    os.mkdir(wspace)

    env_folders = [
        'code/sandbox', 
        'data', 
        'notes', 
        'work/code',
        'configs'
    ]

    for folder in env_folders:
        folder_path = os.path.join(wspace, folder)
        os.makedirs(folder_path)

    print("\nAll folders have been created.\n")
    return