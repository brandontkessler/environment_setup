import shutil
import os

def clear_env(config):
    env = config.get('BASE', 'envdir')
        
    confirmation = input("\nAre you sure you want to clear the existing environment?\n[y/N]\n")

    if confirmation.casefold() == 'y':
        ## Backup the work folder ##
        backup_work_confirm = input("\nDo you want to make a back up of the work folder?\n[Y/n]\n")
        if backup_work_confirm.casefold() in ('y', ''):
            print("\nBacking up `work` (excluding all venvs) in ~/backups/work\n")
            work_loc = os.path.join(env['envdir'], 'work')
            backup_loc = os.path.join(os.path.expanduser('~'), 'backups')
            exclusions = "--exclude 'venv' --exclude '__pycache__' --exclude '*ipynb_checkpoints'"
            os.system(f"rsync -zavP {exclusions} {work_loc} {backup_loc}")

        print("\nClearing environment...\n")
        shutil.rmtree(env['envdir'])
        os.remove('env_config.json')

        print("\nFinished eliminating environment...\n")
    elif confirmation.casefold() in ('n', ''):
        print("\nCanceling...\n")
    else:
        print(f"\nExiting...\nNo command for: {confirmation}. Please select 'y' to confirm.")

    return