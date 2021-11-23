import json
import shutil
import os

def clear_env():
    
    if not os.path.exists('env_config.json'):
        print('\nExiting...\nUnable to find environment config file.')
        return
    # ADD ABILITY TO TAKE INPUT OF PATH IF UNABLE TO FIND CONFIG FILE
    
    with open('env_config.json', 'r') as env_json:
        env = json.load(env_json)
        
    confirmation = input("\nAre you sure you want to clear the existing environment?\n[y/N]\n")

    if confirmation.casefold() == 'y':
        print("\nClearing environment...\n")
        shutil.rmtree(env['envdir'])
        os.remove('env_config.json')
    elif confirmation.casefold() == 'n':
        print("\nCanceling...\n")
    else:
        print(f"\nExiting...\nNo command for: {confirmation}. Please select 'y' to confirm.")

    return