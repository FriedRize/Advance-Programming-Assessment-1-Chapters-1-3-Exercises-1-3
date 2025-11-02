# Initialize counter for loop executions
counter = 0

# Ask the user initially if they want to continue
response = input("Would you like to continue? (Y/N)")

# While loop that continues as long as the user enters 'Y'
while response == 'Y':
    counter += 1
    response = input("Would you like to continue? (Y/N)")

# Output the number of times the loop was executed
print(f"The loop was executed {counter} times.")