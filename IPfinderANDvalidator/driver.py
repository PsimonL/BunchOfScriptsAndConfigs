import re


# https://www.ibm.com/docs/en/networkmanager/4.2.0?topic=translation-private-address-ranges
# Class A: 10.0. 0.0 to 10.255. 255.255.
# Class B: 172.16. 0.0 to 172.31. 255.255.
# Class C: 192.168. 0.0 to 192.168. 255.255.


def get_valid_ips(file_path):
    internal_ips = []
    external_ips = []
    internal_counter, external_counter = 0, 0

    with open(file_path, 'r') as file:
        data = file.read()

        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b' # check if matches pattern IP: a.b.c.d
        ip_matches = re.findall(ip_pattern, data)

        for ip in ip_matches:
            octets = ip.split('.')
            is_valid = len(octets) == 4 and all(0 <= int(octet) <= 255 for octet in octets)
            if is_valid:
                first_octet = int(octets[0])

                if 10 <= first_octet <= 10:  # Class A range internal
                    internal_counter += 1
                    internal_ips.append(ip)
                elif 172 <= first_octet <= 172 and 16 <= int(octets[1]) <= 31:  # Class B range internal
                    internal_counter += 1
                    internal_ips.append(ip)
                elif 192 <= first_octet <= 192 and int(octets[1]) == 168:  # Class C range internal
                    internal_counter += 1
                    internal_ips.append(ip)
                else:  # external range
                    external_counter += 1
                    external_ips.append(ip)

    return internal_ips, external_ips, internal_counter, external_counter


file_path = './file.txt'
internal_ips, external_ips, internal_counter, external_counter = get_valid_ips(file_path)

print("Before execution")
print(f"Number of INTERNAL IPs = {internal_counter} and list:")
print(internal_ips)
print(f"Number of EXTERNAL IPs = {external_counter} and list:")
print(external_ips)
print("Listing done")
