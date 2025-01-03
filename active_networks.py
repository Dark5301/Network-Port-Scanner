#!/usr/local/bin/python3
from scapy.all import IP, ICMP, sr1 
import networks 

#Function to identify active network via ICMP 
def icmp_ping(ip):
    try:
        packet = IP(dst = ip) / ICMP()
        response = sr1(packet, timeout = 10, verbose = 0) 
        if response is not None:
            print(f'Host {ip} is reachable via ICMP.')
            return True 
        else:
            print(f'Host {ip} is not reachable via ICMP.')
            return False 
    except Exception as e:
        print(f'An error occurred: {e}')
        return False
    
#Identifying active networks 
def active_networks():
    active_networks = []
    Networks = networks.process_network()
    for ip in Networks:
        if icmp_ping(ip):
            active_networks.append(ip)
    return active_networks

if __name__ == '__main__':
    #Calling the function
    print('\n')
    print(f'Active networks: {active_networks()}')

