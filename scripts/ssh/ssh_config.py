import os
from textwrap import dedent

def ssh_config():
    ssh_path = os.path.join(os.path.expanduser('~'), '.ssh')

    if not os.path.exists(ssh_path):
        os.mkdir(ssh_path)

    config_file = """\n
        ### Basic Host ###
        # Host dev
        #     HostName dev.example.com
        #     User john
        #     Port 2322

        ### Multi-Jump Host (Jump first to mux1 then to mta1) ###
        # Host jumphost
        # 	HostName mux1.accuenbi.com
        # 	User brandon_kessler
        # 	Port 22
        # 	IdentityFile ~/.ssh/id_rsa
        # 	RequestTTY force
        # 	RemoteCommand ssh mta1

        ### Proxy Jump ###
        # Host *
        # 	ForwardAgent yes

        # Host bastion
        # 	Hostname public.domain.com
        # 	User alex
        # 	Port 50482
        # 	IdentityFile ~/.ssh/id_ed25519

        # Host lanserver
        # 	Hostname 192.168.1.1
        # 	User alex
        # 	ProxyJump bastion
    """

    with open(os.path.join(ssh_path, 'config'), 'a') as f:
        f.write(dedent(config_file))

    os.system(f"chmod 600 {os.path.join(ssh_path, 'config')}")

    print("\nFinished creating the ssh config file in `~/.ssh/config`")

    return
