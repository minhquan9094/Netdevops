import time

from paramiko import client,ssh_exception
from getpass import getpass
import socket

hostname = '172.16.107.132'
username = input("Enter Username:")
port=222


# create command config using list
commands = ['config t', 
            'int lo1001', 
            'ip address 1.1.1.1 255.255.255.0', 
            'end']
cisco_cmd = ['show ip int br']


# check in input username / pass
if not username:
    username = 'admin'
    print(f"No username provided, considering default username {username}")

password = getpass(f"Enter Password of the user {username}: ") or "admin"


# create ssh session

def ssh_session(hostname,port,username,password):

    ssh_client = client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,
                    port=port,
                    username=username,
                    password=password,
                    look_for_keys=False, allow_agent=False)
    print(f"Connected to the device {hostname}")
    return ssh_client


# using invoke shell for multiple command
def _invoke_shell_connect(cmd):
    try:    
        ssh_client=ssh_session(hostname,port,username,password)
        device_access = ssh_client.invoke_shell()
        device_access.send("terminal len 0\n")
        for i in cmd:
            device_access.send(f"{i}\n")
            time.sleep(1)
            # get output msg
            output = device_access.recv(65535)
            print(output.decode(), end='')

        device_access.send("show ip interface br\n")
        time.sleep(2)
        output = device_access.recv(65535)
        print(output.decode())
        ssh_client.close()
    except ssh_exception.NoValidConnectionsError:
        print("SSH Port not reachable")
    except socket.gaierror:
        print("Check the hostname")
    except ssh_exception.AuthenticationException:
        print("Authentication failed, check credentials")


# using exec command for keep session SSH channel
def _exec_command_connect(cmd):
    ssh_client=ssh_session(hostname,port,username,password)
    for i in cmd:
        print(f"\n{'#'*10} Executing {i}{'#'*10}")
        stdin, stdout, stderr = ssh_client.exec_command(i)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(f"Error Occurred: {err}")


_invoke_shell_connect(commands)
time.sleep(1)
_exec_command_connect(cisco_cmd)






### access ssh session cli

# device_access = ssh_client.invoke_shell()
# device_access.send("terminal len 0\n")

'''
device_access.send("show run\n")
time.sleep(2)
output = device_access.recv(65535)
print(output.decode())
ssh_client.close()


'''
