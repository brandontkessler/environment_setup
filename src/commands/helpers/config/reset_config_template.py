import os
import shutil

def reset_config_template():
    shutil.copy('templates/config_template.ini', 'config.ini')