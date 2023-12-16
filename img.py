import scapy.all as scapy
import matplotlib.pyplot as plt

def scan_network(ip):
    # IP Address for the destination
    # Example: '192.168.1.1/24'
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    devices = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices.append(device_info)
    return devices

# Replace with your network IP range
network_devices = scan_network("192.168.1.1/24")

# Dummy data for network load, replace this with real data
network_load = [5, 10, 3, 6] # This should be collected based on actual network load data

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(range(len(network_devices)), network_load, tick_label=[d['ip'] for d in network_devices])
plt.xlabel('Devices')
plt.ylabel('Network Load')
plt.title('Network Load by Device')
plt.show()
