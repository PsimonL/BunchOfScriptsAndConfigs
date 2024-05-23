import subprocess
import socket


def ping(host):
    """
    Ping a host to check connectivity.
    Returns (True, output) if host is reachable, (False, error) otherwise.
    """
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return True, output.decode()
    except subprocess.CalledProcessError as e:
        return False, str(e)


def dns_resolver(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print("DNS resolution working.")
        return True, ip_address
    except socket.error as e:
        print("DNS resolution failed.")
        print(socket.error)
        return False, str(e)


def check_internet_connectivity(ip, domain):
    """
    Check internet connectivity by pinging a known server.
    """
    print(f"Checking connectivity to {ip} using *ping*...")
    flag_ping, mess_ping = ping(google_dns)
    if flag_ping:
        print("Connected to the internet.")
        print(mess_ping)
    else:
        print("No connectivity to the Internet.")
        print("ERROR: ", mess_ping)

    print(f"Checking DNS resolution of {domain}...")
    flag_dns, dns_ip = dns_resolver(domain)
    if flag_dns:
        print(f"DNS resolution working. IP address for {google_domain} is {dns_ip}")
    else:
        print("No DNS record found.")
        print("ERROR: ", dns_ip)


def check_wifi_connections():
    """
    Check available Wi-Fi networks and current connection status.
    """
    try:
        print("Available Wi-Fi networks:")
        available_networks = subprocess.check_output(['nmcli', 'dev', 'wifi', 'list'])
        print(available_networks.decode())

        print("Current Wi-Fi connection status:")
        connection_status = subprocess.check_output(['nmcli', 'con', 'show', '--active'])
        print(connection_status.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute nmcli command: {e}")


if __name__ == "__main__":
    print("Checking internet connectivity...")
    google_dns = "8.8.8.8"
    google_domain = "www.google.com"
    check_internet_connectivity(ip=google_dns, domain=google_domain)
    # print("\nChecking Wi-Fi connections...")
    # check_wifi_connections()
