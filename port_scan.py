#!/usr/local/bin/python3
import socket 
import active_networks

#Identify open ports on active networks 
def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((ip, port))
                if result == 0:
                    try:
                        #Get the service name for the port (TCP)
                        service = socket.getservbyport(port, 'tcp')
                    except:
                        service = 'Unknown service'
                    open_ports.append((port, service))
        except Exception as e:
            pass 
    return open_ports

def port_scanning():
    #Scan ports 1-1024 on active networks
    target_ips = active_networks.active_networks()

    #Scan each IP 
    for ip in target_ips:
        open_ports = scan_ports(ip, 1, 1025)
        if open_ports:
            print(f'Open ports on {ip}:')
            for port, service in open_ports:
                print(f'    Port {port}: {service}')
        else:
            print(f'No open ports found on {ip}')

if __name__ == '__main__':
    #Calling the function 
    port_scanning() 