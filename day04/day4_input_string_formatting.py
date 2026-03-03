# User Input Collection
print("===SECURITY SCAN SETUP===")
analyst_name = input("Enter analyst name: ")
target_ip = input("Enter target IP: ")
port_start = int(input("Enter start port: "))
port_end = int(input("Enter end port: "))
threat_score = float(input("Enter threat score(0.0-10.0): "))

#Calculations
total_ports = port_end - port_start

#Formatted Report
print(f"""
=== SCAN CONFIGURATION ===
Analyst: {analyst_name.upper()}
Target: {target_ip}
Port Range: {port_start} - {port_end}
Total Ports: {total_ports:,}
Threat Score: {threat_score:.1f}/10.0
Risk Level: HIGH
====================
""")
