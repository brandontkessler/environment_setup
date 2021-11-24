import os
from textwrap import dedent

def ssh_setup():
    ssh_path = os.path.join(os.path.expanduser('~'), '.ssh')

    config_file = """
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

    if not os.path.exists(ssh_path):
        os.mkdir(ssh_path)
    
    with open(os.path.join(ssh_path, 'config'), 'a') as f:
        f.write(dedent(config_file))

    os.system(f"chmod 600 {os.path.join(ssh_path, 'config')}")

    print("\nFinished creating the ssh config file in `~/.ssh/config`")

    key_confirm = input("\nDo you want to generate a new rsa keypair?\n[Y/n]\n")
    
    if key_confirm.casefold() in ('y', ''):
        key_name_input = input("Provide name or press enter for default (id_rsa) : ")
        key_name = 'id_rsa' if key_name_input == '' else key_name_input
        os.system(f"ssh-keygen -t rsa -b 4096 -f {os.path.join(ssh_path, key_name)}")
        print("\nFinished rsa keygen\n")
    else:
        print("\nSkipping rsa keygen\n")

    return
