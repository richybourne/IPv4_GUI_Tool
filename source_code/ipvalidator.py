import ipaddress

def validate_ips_no_subnet(ips):
    for ip in ips:
        if not validate_ip(ip):
            return False
    return True

def validate_ip_no_subnet(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

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