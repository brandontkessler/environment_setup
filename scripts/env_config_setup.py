import json
import os
import sys

def env_config_setup(envdir):

    env_config = {'envdir': envdir}

    with open(os.path.join(envdir, 'config', 'env_config.json'), 'w') as f:
        f.write(json.dumps(env_config, indent=4))

    print("\nConfig files have been created in environment_setup and Environment\n")

    return
