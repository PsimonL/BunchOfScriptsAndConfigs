import re

# https://www.ibm.com/docs/en/networkmanager/4.2.0?topic=translation-private-address-ranges
# Class A: 10.0. 0.0 to 10.255. 255.255.
# Class B: 172.16. 0.0 to 172.31. 255.255.
# Class C: 192.168. 0.0 to 192.168. 255.255.

def get_valid_ips(file_path):
    pass

file_path = './file.txt'
internal_ips, external_ips = get_valid_ips(file_path)

print("Internal IPs:")
print(internal_ips)
print("External IPs:")
print(external_ips)