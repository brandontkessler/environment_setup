from scripts.cleanup.clear_workspace import clear_env
import helpers as h

config = h.read_config('.workspace_config.ini')

clear_env(config)