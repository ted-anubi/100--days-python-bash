# Network Math
total_hosts = 254
active_hosts = 37
inactive_hosts = total_hosts - active_hosts

print(f"Total Hosts: {total_hosts}")
print(f"Active Hosts: {active_hosts}")
print(f"Inactive Hosts: {inactive_hosts}")
print(f"Active Percentage: {round((active_hosts / total_hosts) * 100, 2)}%")

#Port Calculations
start_port = 1024
end_port = 65535
total_ports = end_port - start_port
print(f"\nTotal Ports Available: {total_ports}")
print(f"Ports per range: {total_ports // 4}")

#Type Conversion
port_string = "443"
port_number = int(port_string)
print(f"\nHTTPS port: {port_number}")
print(f"Next Port: {port_number + 1}")
print(type(port_number))

#User Input
target = input("\nEnter target IP to scan: ")
ports = input("How many ports to scan: ")
ports = int(ports)
print(f"\nScanning {target} across {ports} ports...")
print(f"Scan will check ports 1 to {ports}")
