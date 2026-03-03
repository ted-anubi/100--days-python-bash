#User Input Collection
print("=== THREAT ASSESSMENT SETUP ===")
assessor_name = input("Enter assessor name: ")
Target_Host = input("Enter target host: ")
Vulnerabilities_found = int(input("Enter vulnerabilities: "))
Highest_CVSS_Score = float(input("Enter highest cvss score(0.0-10.0)/10.0: "))
Time_Spent = float(input("Enter time spent: "))

#Calculations
Average_per_vuln = Time_Spent/Vulnerabilities_found


#Formatted Report
print(f"""
=== THREAT ASSESSMENT REPORT ===
Assessor: {assessor_name.upper()}
Target: {Target_Host}
Vulnerabilities Found: {Vulnerabilities_found}
Highest CVSS Score: {Highest_CVSS_Score}/10.0
Time Spent: {Time_Spent} hours
Average per vuln: {Average_per_vuln:.2f} hours
Risk Rating: CRITICAL
=======================
""")