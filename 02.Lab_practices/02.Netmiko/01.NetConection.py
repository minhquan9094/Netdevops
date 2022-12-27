from netmiko import Netmiko

from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler


cisco_device = {
    'device_type': 'cisco_ios',
    'host':   '172.16.107.132',
    'username': 'quandm',
    'password': 'quandm'
}


cisco_device_autodetect = {
    'device_type': 'autodetect',
    'host':   '172.16.107.132',
    'username': 'quandm',
    'password': 'quandm'
}


# Using send_command to send show / execute command

net_connect = Netmiko(**cisco_device)
print("Connected successfully")
cmd_output = net_connect.send_command("show ip int brief")
#cmd_output = net_connect.send_command("ping 172.16.107.132 repeat 5", read_timeout=20, expect_string=r"c.+#")
print(cmd_output)





#  Using send_config_set to deploy config / import from file

commands = [f'int lo1001',
            f'ip address 192.1.1.10 255.255.255.0',
            'no shut']

config = net_connect.send_config_set(commands)
# config = net_connect.send_config_from_file(config_file='config.txt')
print(config)
print(net_connect.send_command("show ip int brief"))
net_connect.disconnect()



# Using Auto Detect

guesser = SSHDetect(**cisco_device_autodetect)
best_match = guesser.autodetect()
print("Best match is: {0}".format(best_match)) # Name of the best device_type to use further
print(guesser.potential_matches) # Dictionary of the whole matching result
cisco_device_autodetect['device_type'] = best_match
print (cisco_device_autodetect)

connection = ConnectHandler(**cisco_device_autodetect)
print(connection.send_command("show version | inc up"))

