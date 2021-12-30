from textwrap import dedent
import os

from src.commands.scripts import bash
from src.commands.helpers import config as c


def test_bash_aliases(tmpdir):
    f = tmpdir.mkdir('tmp').join('bash_aliases.txt')
    bash.bash_aliases(f.strpath)

    with open('src/commands/scripts/bash/static/bash_aliases.txt', 'r') as ba:
        assert f.read() == ba.read()
    

def test_bash_functions(tmpdir):
    config = c.read_config('tests/configs/test_config.ini')
    wspace = config.get('BASE', 'wspace')
    weather_path = os.path.join(wspace, 'code', 'daily_weather')

    f = tmpdir.mkdir('tmp').join('bash_functions.txt')
    bash.bash_functions(config, f.strpath)

    with open('src/commands/scripts/bash/static/bash_functions.txt', 'r') as bf:
        assert f.read() == bf.read().replace('<weather_path>', weather_path)


def test_bash_profile(tmpdir):
    config = c.read_config('tests/configs/test_config.ini')
    wspace = config.get('BASE', 'wspace')

    bash_profile_additions = """
        if [ -f ~/.bashrc ]; then
            source ~/.bashrc
        fi
    """

    f = tmpdir.mkdir('tmp').join('bash_profile.txt')
    bash.bash_profile(f.strpath)

    assert f.read() ==  dedent(bash_profile_additions)


def test_bash_prompt(tmpdir):
    f = tmpdir.mkdir('tmp').join('bash_prompt.txt')
    bash.bash_prompt(f.strpath)

    with open('src/commands/scripts/bash/static/bash_prompt.txt', 'r') as ba:
        assert f.read() == ba.read()


def test_bashrc(tmpdir):
    config = c.read_config('tests/configs/test_config.ini')
    wspace = config.get('BASE', 'wspace')
    codespace = os.path.join(wspace, 'code')

    f = tmpdir.mkdir('tmp').join('bashrc.txt')
    bash.bashrc_setup(config, f.strpath)

    with open('src/commands/scripts/bash/static/bashrc.txt', 'r') as brc:
        assert f.read() == brc.read().replace('<workspace/code>', codespace)


def test_bash_setup(tmpdir):
    config = c.read_config('tests/configs/test_config.ini')
    wspace = config.get('BASE', 'wspace')
    weather_path = os.path.join(wspace, 'code', 'daily_weather')

    bash_profile_additions = """
        if [ -f ~/.bashrc ]; then
            source ~/.bashrc
        fi
    """

    tmp = tmpdir.mkdir('tmp')
    bash.bash_setup(config, tmp)

    with open('src/commands/scripts/bash/static/bashrc.txt', 'r') as brc:
        assert tmp.join('.bashrc').read() == brc.read().replace('<workspace/code>', os.path.join(wspace, 'code'))

    with open('src/commands/scripts/bash/static/bash_prompt.txt', 'r') as ba:
        assert tmp.join('.bash_prompt').read() == ba.read()

    assert tmp.join('.bash_profile').read() ==  dedent(bash_profile_additions)

    with open('src/commands/scripts/bash/static/bash_functions.txt', 'r') as bf:
        assert tmp.join('.bash_functions').read() == bf.read().replace('<weather_path>', weather_path)

    with open('src/commands/scripts/bash/static/bash_aliases.txt', 'r') as ba:
        assert tmp.join('.bash_aliases').read() == ba.read()