from .scripts import cleanup
from .helpers import config as config_helper

def teardown(workspace_path):
    config = config_helper.read_config(workspace_path)
    cleanup.clear_workspace(config)