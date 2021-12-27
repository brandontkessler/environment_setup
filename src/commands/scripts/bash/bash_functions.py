import os
from textwrap import dedent

def bash_functions(config):
    wspace = config.get('BASE', 'wspace')
    basedir = os.path.expanduser('~')
    
    weather_path = os.path.join(wspace, 'code', 'daily_weather')
    bash_functions = fr"""
        function test_function() {{
            echo "Some test foo!"
            echo "Another line"
        }}

        function weather() {{
            source {weather_path}/venv/bin/activate
            python weather.py
            deactivate
        }}
    """

    with open(os.path.join(basedir, '.bash_functions'), 'a') as f:
        f.write(dedent(bash_functions))

    print("\nBash functions have been set up.\n")

    return
