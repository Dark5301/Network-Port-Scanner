#!/usr/local/bin/python3
import ipaddress

# Function for identifying the network 
def process_network():
    n = input('Enter the target network range (e.g., 192.168.1.0/24): ')
    try:
        net = ipaddress.IPv4Network(n, strict = False)
        net_list = [str(ip) for ip in net.hosts()]
        net_num = net.num_addresses
        print(f'Usuable hosts: {net_list}\n')
        print(f'Total number of hosts: {net_num}')
        return net_list
    except ValueError:
        print('Invalid network range') 

if __name__ == '__main__':
    # Calling the function
    process_network()

