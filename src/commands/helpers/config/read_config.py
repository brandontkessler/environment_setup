from configparser import ConfigParser


def read_config(fpath):
    config = ConfigParser()
    config.read(fpath)
    
    return config