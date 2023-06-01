import ipaddress

def perform_ipv4_best_match_lookup(destination_ip, networks):
    # Step 1: Convert the destination and networks to binary
    destination_ip_binary = '{:#b}'.format(ipaddress.IPv4Address(destination_ip))
    destination_ip_binary = destination_ip_binary[2:]

    # Make a new array of tuples, the left having the binary network address and the right having the subnet mask
    binary_networks = []
    for network in networks:
        bin_network = network.split('/')[0]
        bin_network = '{:#b}'.format(ipaddress.IPv4Address(bin_network))
        bin_network = bin_network[2:]
        binary_networks.append(bin_network)
    bin_networks_tuple = []
    for i in range(len(binary_networks)):
        bin_networks_tuple.append((binary_networks[i], networks[i].split('/')[1]))

    # Cut each binary network address to the length of the subnet mask
    final_cut_networks = [(network[0][:int(network[1])], network[1]) for network in bin_networks_tuple]

    # Step 2: Find the longest common prefix (number of matching bits)
    longest_match_subnet = 0
    longest_match_index = 0
    for i in range(len(final_cut_networks)):
        current_network = final_cut_networks[i][0]
        current_subnet_mask = final_cut_networks[i][1]
        temp_destination_ip = destination_ip_binary[:int(current_subnet_mask)]
        if temp_destination_ip == current_network:
            if int(current_subnet_mask) > longest_match_subnet:
                longest_match_subnet = int(current_subnet_mask)
                longest_match_index = i

    # Step 3: Return the network address and subnet mask of the longest match
    if longest_match_subnet == 0:
        return 'No match found'

    return networks[longest_match_index]

    


    