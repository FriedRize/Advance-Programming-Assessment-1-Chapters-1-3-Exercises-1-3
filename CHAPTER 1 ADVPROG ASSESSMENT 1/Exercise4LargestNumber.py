# Prompt the user for three numbers
print("Enter the first number:")
num1 = float(input())
print("Enter the second number:")
num2 = float(input())
print("Enter the third number:")
num3 = float(input())

# Use multiple if-else statements to find the largest
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Output the largest number
print(f"The largest number is: {largest}")