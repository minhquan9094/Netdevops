
'''
Script to using logging library get output 


'''

from netmiko import ConnectHandler
import logging
logging.basicConfig(filename='demo_netmiko.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
csr = {
    'device_type': 'cisco_ios',
    'host': '172.16.107.132',
    'username': 'quandm',
    'password': 'quandm'
}

net_connect = ConnectHandler(**csr)
logger.info("Connected")
print("Connected successfully")
show_cmd = net_connect.send_command("show tech-support")

with open('sh_output.txt', 'w') as file:
    logger.info("Writing content to file")
    file.write(show_cmd)
