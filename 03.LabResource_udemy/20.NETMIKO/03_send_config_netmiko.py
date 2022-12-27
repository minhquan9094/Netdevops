from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host':   '172.16.107.132',
    'username': 'quandm',
    'password': 'quandm'
}

commands = [f'int lo1001',
            f'ip address 11.1.1.10 255.255.255.0',
            'no shut']
net_connect = Netmiko(**csr)
print("Connected successfully")
config = net_connect.send_config_set(commands)
#config = net_connect.send_config_from_file(config_file='config.txt')
print(config)
print(net_connect.send_command("show ip int brief"))
net_connect.disconnect()
