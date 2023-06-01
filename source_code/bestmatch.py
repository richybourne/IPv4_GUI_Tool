import ipaddress

def perform_ipv4_best_match_lookup(destination_ip, networks):
    # Step 1: Convert the destination and networks to binary
    destination_ip = destination_ip.split('/')[0]
    destination_ip = '{:#b}'.format(ipaddress.IPv4Address(destination_ip))
    destination_ip = destination_ip[2:]

    binary_networks = []
    for network in networks:
        network = network.split('/')[0]
        network = '{:#b}'.format(ipaddress.IPv4Address(network))
        network = network[2:]
        binary_networks.append(network)

    # Step 2: Find the longest common prefix (number of matching bits)
    current_longest_prefix = 0
    current_longest_prefix_network = None
    for network in binary_networks:
        number_of_matching_bits = 0
        for i in range(len(network)):
            if network[i] == destination_ip[i]:
                number_of_matching_bits += 1
            else: break
        if number_of_matching_bits > current_longest_prefix:
            current_longest_prefix = number_of_matching_bits
            current_longest_prefix_network = network
    
    # Step 3: Copy the matching bits and add all 0 bits to determine the network address
    network_address = current_longest_prefix_network[:current_longest_prefix]
    network_address += '0' * (32 - current_longest_prefix)
    network_address = ipaddress.IPv4Address(int(network_address, 2))

    # Turn the address and subnet mask into a CIDR notation
    return str(network_address) + '/' + str(current_longest_prefix)

    