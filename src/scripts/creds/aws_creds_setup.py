import os
from textwrap import dedent

def aws_creds_setup(config):
    if config.getboolean('AWS', 'setupAwsKeys') is True:
        access_key = config.get('AWS', 'awsAccessKeyId', fallback='')
        secret_key = config.get('AWS', 'awsSecretAccessKey', fallback='')
        region = config.get('AWS', 'region', fallback='')

        aws_path = os.path.join(os.path.expanduser('~'), '.aws')

        if os.path.exists(os.path.join(aws_path, 'credentials')):
            print("\nSkipping...\naws credentials already set up in `~/.aws/credentials`\n")
            return

        if not os.path.exists(aws_path):
            os.mkdir(aws_path)

        with open(os.path.join(aws_path, 'credentials'), 'w') as f:
            creds_setup = f"""
                [default]
                aws_access_key_id = {access_key}
                aws_secret_access_key = {secret_key}
                region = {region}
            """

            f.write(dedent(creds_setup).strip())
        
        print("\naws credentials set up in `~/.aws/credentials/\n")
    
    else:
        print("\nSkipping AWS Credential setup\n")

    return