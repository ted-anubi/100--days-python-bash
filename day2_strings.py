#String basics
hacker_name = "Anonymous"
ip_address = "192.168.1.100"
attack_type = "SQL Injection"
location = "Unknown"

#Concatenation
full_profile = hacker_name + " | " + ip_address + " | " + attack_type
print(full_profile)

#Length
print(len(ip_address))
print(len(attack_type))

#Indexing
print(ip_address[0])
print(ip_address[-1])

#Slicing
print(ip_address[0:3])

#Methods
print(attack_type.upper())
print(attack_type.lower())
print(attack_type.replace("SQL Injection", "XSS Attack"))

#f-string
print(f"Hacker:{hacker_name} | IP: {ip_address} | Attack: {attack_type} | Location: {location}")