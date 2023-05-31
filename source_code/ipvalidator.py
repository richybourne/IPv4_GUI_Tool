import ipaddress

def validate_ips(ips):
    for ip in ips:
        if not validate_ip(ip):
            return False
    return True

def validate_ip(ip):
    try:
        ipaddress.ip_network(ip)
        return True
    except ValueError:
        return False