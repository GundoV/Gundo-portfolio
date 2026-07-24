print("=" * 40)
print("     MULTI-FUNCTION CALCULATOR     ")
print("=" * 40)

# 1. Collect inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 2. Perform Calculations
add = round(num1 + num2, 2)
sub = round(num1 - num2, 2)
mul = round(num1 * num2, 2)

# Division safety check
if num2 != 0:
    div = round(num1 / num2, 2)
    floor_div = round(num1 // num2, 2)
    mod = round(num1 % num2, 2)
else:
    div = "Error: Division by 0"
    floor_div = "Error: Division by 0"
    mod = "Error: Division by 0"

# 3. Formatted Table Output
print("\n" + "=" * 40)
print(f"| {'Operation':<18} | {'Result':<15} |")
print("=" * 40)
print(f"| {'Addition (+)':<18} | {str(add):<15} |")
print(f"| {'Subtraction (-)':<18} | {str(sub):<15} |")
print(f"| {'Multiplication (*)':<18} | {str(mul):<15} |")
print(f"| {'Division (/)':<18} | {str(div):<15} |")
print(f"| {'Floor Div (//)':<18} | {str(floor_div):<15} |")
print(f"| {'Modulus (%)':<18} | {str(mod):<15} |")
print("=" * 40)