from scripts.cleanup.clear_env import clear_env
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
testing = config.getboolean('TEST', 'active')

clear_env(config)