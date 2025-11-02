# Ask the user to enter a number
num = int(input("Enter a number: "))

# Initialize sum
sum_of_digits = 0

# Use a loop to extract each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10

# Display the result
print(f"The sum of digits in {num} is: {sum_of_digits}")