# Prompt the user for two integers
print("Enter the first integer:")
num1 = int(input())
print("Enter the second integer:")
num2 = int(input())

# Perform calculations
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2

# Handle division by zero for quotient and remainder
if num2 != 0:
    quotient_result = num1 / num2
    remainder_result = num1 % num2
else:
    quotient_result = "Undefined (division by zero)"
    remainder_result = "Undefined (division by zero)"

# Output the results
print(f"Sum (+): {sum_result}")
print(f"Diff (-): {diff_result}")
print(f"Product (x): {product_result}")
print(f"Quotient (/): {quotient_result}")
print(f"Remainder (%): {remainder_result}")