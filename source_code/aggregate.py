import ipaddress

def perform_ipv4_route_aggregation(networks):
    # Step 1: Convert the networks to binary
    binary_networks = []
    for network in networks:
        network = network.split('/')[0]
        network = '{:#b}'.format(ipaddress.IPv4Address(network))
        network = network[2:]
        binary_networks.append(network)
        
    # Step 2: Find the longest common prefix (number of matching bits)
    number_of_matching_bits = 0
    first_network = binary_networks[0]
    exit = False
    for i in range(len(first_network)):
        for network in binary_networks[1:]:
            if network[i] != first_network[i]:
                subnet_mask = number_of_matching_bits
                exit = True
                break
        if not exit:
            number_of_matching_bits += 1
        else: break
        
    #Step 3: Copy the matching bits and add all 0 bits to determine the network address
    network_address = first_network[:number_of_matching_bits]
    network_address += '0' * (32 - number_of_matching_bits)
    network_address = ipaddress.IPv4Address(int(network_address, 2))
    
    # Turn the address and subnet mask into a CIDR notation
    return str(network_address) + '/' + str(subnet_mask)

