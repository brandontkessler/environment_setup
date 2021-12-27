import os

def setup_bcreds(config):
    wspace = config.get('BASE', 'wspace')

    os.system(f"touch {os.path.join(wspace, 'code', 'bcreds.json')}")
    os.system(f"touch {os.path.join(wspace, 'work', 'code', 'bcreds.json')}")
    
    return