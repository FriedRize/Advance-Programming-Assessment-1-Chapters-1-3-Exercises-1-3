# Ask user to enter number of days
days = int(input("Enter the number of days: "))

# Convert days to hours, hours to minutes, and minutes to seconds
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Display the result
print(f"\nNumber of days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")