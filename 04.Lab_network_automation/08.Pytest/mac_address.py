# filename: mac_address.py

### def to parse mac address
def normalize_mac_address(mac):
    print (mac)
    if mac.count(".") == 2:
        mac = f"{mac[0:2]}:{mac[2:4]}:{mac[5:7]}:{mac[7:9]}:{mac[10:12]}:{mac[12:14]}"
    return mac
