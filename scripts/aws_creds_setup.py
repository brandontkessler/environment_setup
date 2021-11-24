import os
from textwrap import dedent

def aws_creds_setup():
    aws_path = os.path.join(os.path.expanduser('~'), '.aws')

    if os.path.exists(os.path.join(aws_path, 'credentials')):
        print("\nExiting...\naws credentials already set up in `~/.aws/credentials`")
        return

    if not os.path.exists(aws_path):
        os.mkdir(aws_path)

    with open(os.path.join(aws_path, 'credentials'), 'w') as f:
        creds_setup = """
            [default]
            aws_access_key_id = ABCDEFG
            aws_secret_access_key = abcdefghijklmnop
            region = us-east-1
        """

        f.write(dedent(creds_setup).strip())
    
    print("\naws credentials set up in `~/.aws/credentials/\n")
    print("Replace the dummy credentials with actuals when provided.")
    return