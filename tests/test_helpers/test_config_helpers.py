from src.commands.helpers import config as c

def test_read_config():
    main = c.read_config('config.ini')
    assert main.get('GIT', 'username') == 'brandontkessler'


def test_read_config_template():
    template = c.read_config('templates/config_template.ini')
    assert template.get('GIT', 'username') == 'brandontkessler'

