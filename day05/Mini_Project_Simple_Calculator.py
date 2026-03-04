#Simple Calculator
print("=== SIMPLE CALCULATOR ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation(+,-,*,/): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print(f"""
=== RESULT ===
{num1}){operation}{num2} = {result:.2f}
===============
""")

