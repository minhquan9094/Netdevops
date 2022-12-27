from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler

csr = {
    'device_type': 'cisco_ios',
    'host': '172.16.107.132',
    'username': 'quandm',
    'password': 'quandm'
}

CSW = {
    'device_type': 'autodetect',
    'host': '172.16.107.10',
    'username': 'quandm',
    'password': 'quandm'
}


# Using Auto Detect

guesser = SSHDetect(**CSW)
best_match = guesser.autodetect()
print("Best match is: {0}".format(best_match)) # Name of the best device_type to use further
print(guesser.potential_matches) # Dictionary of the whole matching result
CSW['device_type'] = best_match
print (CSW)


device_list = [csr, CSW]

for device in device_list:
    with ConnectHandler(**device) as net_connect:
        print("Connected successfully")
        show_cmd = net_connect.send_command("show ip interface brief")
        print(show_cmd)

    


