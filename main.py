import ipaddress

interface = ipaddress.ip_interface("10.10.254.96/24")
network = interface.network

print("My IP:", interface.ip)
print("Network:", network.network_address)
print("Broadcast:", network.broadcast_address)
print("Subnet mask:", network.netmask)
print("Total addresses:", network.num_addresses)

#python3 -m http.server 8080 --bind 127.0.0.1
