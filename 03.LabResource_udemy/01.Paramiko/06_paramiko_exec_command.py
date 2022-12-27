import time
from paramiko import client
from getpass import getpass


linux_cmd = ['ls -larth', 'echo $USER', 'hostname', 'sdfgh']
cisco_cmd = ['show ver12']

def exec_cmd_executor(hostname, commands, username, password):
    print(f"Connecting to the device {hostname}..")
    ssh_client = client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                       allow_agent=False)

    print(f"Connected to the device {hostname}")

    for cmd in commands:
        print(f"\n{'#'*10} Executing {cmd}{'#'*10}")
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(f"Error Occurred: {err}")


exec_cmd_executor('192.168.0.19', linux_cmd, 'evolve', 'evolve@123')
exec_cmd_executor('csr1.test.lab', cisco_cmd, 'admin', 'admin')
