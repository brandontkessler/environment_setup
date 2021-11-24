import os
import sys
import shutil

def folder_structure(envdir):

    if os.path.exists(envdir):
        msg = "An 'Environment' folder already exists in the root directory. Delete and rebuild?\n[y/N]\n"
        env_exists_response = input(msg)

        if env_exists_response.casefold() != 'y'.casefold(): 
            sys.exit("\nExiting...\nInput of 'y' needed to continue.")

        print("Clearing existing 'Environment' folder in root directory.")
        shutil.rmtree(envdir)

    os.mkdir(envdir)

    env_folders = [
        'code/sandbox', 
        'data', 
        'notes', 
        'work/notes', 
        'work/code/python', 
        'work/code/r', 
        'work/code/sql',
        'config'
    ]

    for folder in env_folders:
        folder_path = os.path.join(envdir, folder)
        os.makedirs(folder_path)

    print("\nAll folders have been created.\n")
    return