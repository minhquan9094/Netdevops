### Multiple task using concurrent.futures 

from netmiko import ConnectHandler, exceptions
from datetime import datetime
import concurrent.futures as cf

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

hosts = [csr, CSW]
start_time = datetime.now()
print (start_time)

def netmiko_connect(**device):
    try:
        net_connect = ConnectHandler(**device)
        print(f"Connected Successfully to the Device: {device['host']}")
        output = net_connect.send_command('show ip int brief')
        # print(output)
        print(f"Writing output to the File: {device['host']}.txt")
        with open(f"{device['host']}.txt", 'w') as data:
            data.write(output)
        net_connect.disconnect()
    except exceptions.NetmikoAuthenticationException:
        print(f"Authentication failed on {device['host']}")
    except exceptions.NetmikoTimeoutException:
        print(f"Session timeout on {device['host']}")

with cf.ThreadPoolExecutor() as executor:
    total_output = [executor.submit(netmiko_connect, **host) for host in hosts]

end_time = datetime.now()
print(end_time - start_time)