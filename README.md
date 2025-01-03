# Network and Port Scanning Tool

This Python-based tool helps you scan a network range for active devices, detect open ports on these devices, and identify the services running on the open ports. It is divided into three components, each with a specific functionality.

## Features
1. **Identify Active Devices**: Uses ICMP ping to determine whether hosts in the network range are reachable.
2. **Scan Ports**: Scans a range of ports (default: 1-1024) on active devices to identify open ports.
3. **Detect Services**: Maps services running on open ports to their respective port numbers.

## Components

### 1. `networks.py`
- **Purpose**: To process the input network range and generate a list of usable IP addresses.
- **Functionality**:
  - Prompts the user for a network range (e.g., `192.168.1.0/24`).
  - Generates a list of usable IP addresses within the given range.
  - Displays the total number of usable hosts.
- **Usage**:
  Run this script to generate the list of IPs for scanning.

### 2. `active_networks.py`
- **Purpose**: To identify active devices in the network using ICMP ping.
- **Functionality**:
  - Sends ICMP packets to each IP address in the network range.
  - Checks for reachable devices.
  - Returns a list of active IP addresses.
- **Usage**:
  Run this script after generating the network range to identify active devices.

### 3. `port_scan.py`
- **Purpose**: To scan open ports and identify services on the active devices.
- **Functionality**:
  - Accepts a list of active devices from `active_networks.py`.
  - Scans ports (default: 1-1024) for each active device.
  - Identifies services running on open ports.
  - Displays the results.
- **Usage**:
  Run this script after identifying active devices to scan their open ports and services.

---

## Installation
1. Install Python 3.x if not already installed.
2. Install required dependencies:
   ```bash
   pip install scapy
   ```

---

## How to Use
1. **Process Network**:
   Run `networks.py` to input a network range and generate usable IP addresses.
   ```bash
   python3 networks.py
   ```
   Example input:
   ```
   Enter the target network range (e.g., 192.168.1.0/24): 192.168.1.0/24
   ```

2. **Identify Active Devices**:
   Run `active_networks.py` to detect reachable devices.
   ```bash
   python3 active_networks.py
   ```
   Example output:
   ```
   Host 192.168.1.1 is reachable via ICMP.
   Host 192.168.1.5 is reachable via ICMP.
   Active networks: ['192.168.1.1', '192.168.1.5']
   ```

3. **Scan Ports**:
   Run `port_scan.py` to scan open ports on active devices and identify running services.
   ```bash
   python3 port_scan.py
   ```
   Example output:
   ```
   Open ports on 192.168.1.1:
       Port 80: http
       Port 443: https
   Open ports on 192.168.1.5:
       Port 22: ssh
   ```

---

## Notes
- Ensure you have the necessary permissions to run ICMP ping and scan ports on the target network.
- The port range can be adjusted in the `scan_ports` function in `port_scan.py`.
- The `socket.getservbyport()` function is used to identify services, but it might not map all ports to services.

---

## Disclaimer
This tool is intended for educational purposes and authorized use only. Unauthorized scanning of networks may be illegal and unethical. Always obtain proper permissions before scanning a network.

