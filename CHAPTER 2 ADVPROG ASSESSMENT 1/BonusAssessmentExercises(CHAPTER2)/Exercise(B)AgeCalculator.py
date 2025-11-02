from datetime import date, datetime

# Ask user for date of birth
dob_input = input("Enter your date of birth (dd/mm/yyyy): ")

# Convert input string to date object
dob = datetime.strptime(dob_input, "%d/%m/%Y").date()

# Get today's date
today = date.today()

# Calculate age
age = today.year - dob.year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

# Display the result
print(f"Your age is {age} years.")