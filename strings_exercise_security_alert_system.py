#String basics
alert_level = "CRITICAL"
target_ip = "10.0.0.254"
attack_method = "brute force"
timestamp = "2026-02-28  06:00:00"
analyst = "Teddy Anubi"

#String methods & f-strings
print("=== SECURITY ALERT === ")
print(f"Level: {alert_level}")
print(f"Target IP: {target_ip}")
print(f"Attack: {attack_method.upper()}")
print(f"Time: {timestamp}")
print(f"Assigned To: {analyst.upper()}")
print(f"IP First Octet: {target_ip[0:2]}")
print(f"Alert Length: {len(alert_level)}")
print("=" * 22)
