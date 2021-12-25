import os

def setup_bcreds(config):
    envdir = config.get('BASE', 'envdir')

    os.system(f"touch {os.path.join(envdir, 'code', 'bcreds.json')}")
    os.system(f"touch {os.path.join(envdir, 'work', 'code', 'bcreds.json')}")
    
    return