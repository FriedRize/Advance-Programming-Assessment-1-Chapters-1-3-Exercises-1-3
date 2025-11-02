print("Hello, user!")
print("What is your name?")
name = input()
print("What is your age?")
age = int(input())

# Title case the name
formatted_name = name.title()

# Calculate length of the name
name_length = len(name)

# Calculate age after one year
future_age = age + 1

# Print the output in the specified format
print(f"It is good to meet you, {formatted_name}")
print("The length of your name is:")
print(name_length)
print(f"You will be {future_age} in a year.")