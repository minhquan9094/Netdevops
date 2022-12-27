import napalm
import json

csr = {
    'hostname': '172.16.107.132',
    'username': 'quandm',
    'password': 'quandm'
}

dev_type= 'ios'
driver = napalm.get_network_driver(dev_type)
device= driver(**csr)
device.open()
print("Connected successfully")

output = device.get_arp_table()
print (output)
print(json.dumps(output, indent=2))
device.close()

