from netmiko import Netmiko,ConnectHandler, file_transfer, progress_bar

csr = {
    'device_type': 'cisco_ios',
    'host': '172.16.107.132',
    'username': 'quandm',
    'password': 'quandm'
}

net_connect = Netmiko(**csr)
print("Connected successfully")


##### Upload file to Device

# transfer = file_transfer(net_connect,
#                          source_file='scp_txt.txt',
#                          dest_file='scp_txt.txt',
#                          file_system='nvram:',
#                          direction='put',
#                          overwrite_file=True,
#                          progress4=progress_bar)


### Download file from device
### Example: backup configuration
transfer = file_transfer(net_connect,
                         source_file='startup-config',
                         dest_file='backkup_startup-config',
                         file_system='nvram:',
                         direction='get',
                         overwrite_file=True,
                         progress4=progress_bar)



print(transfer)
net_connect.disconnect()