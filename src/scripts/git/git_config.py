import os

def git_config(config):
    if config.getboolean('GIT', 'setupGitConfig') is True:
        username = config.get('GIT', 'userName', fallback='')
        email = config.get('GIT', 'userEmail', fallback='')

        os.system(f'git config --global user.name "{username}"')
        os.system(f'git config --global user.email {email}')

        personal_access_token = config.get('GIT', 'personalAccessToken', fallback='')

        cmd = f'security add-internet-password -a {username}'
        cmd += f' -r htps -w {personal_access_token}'
        cmd += ' -l github.com -s github.com '
        cmd += '-T /Library/Developer/CommandLineTools/usr/libexec/git-core/git-credential-osxkeychain'

        os.system(cmd)
        print('Git now configured')
        print('\n')

    else:
        print('Git config skipped')

    return