import json
import os
import sys

def env_config_setup(envdir):

    env_config = {'envdir': envdir}

    with open(os.path.join(envdir, 'config', 'env_config.json'), 'w') as env_json:
        json.dump(env_config, env_json)

    print("\nConfig files have been created in environment_setup and Environment\n")

    return
