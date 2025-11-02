# Create an integer list with 10 values
int_list = [12, 45, 7, 89, 23, 56, 34, 78, 90, 11]

# Output the list using a for loop
print("Original list:")
for num in int_list:
    print(num, end=' ')
print()  # Newline

# Output the highest and lowest value
highest = max(int_list)
lowest = min(int_list)
print(f"Highest value: {highest}")
print(f"Lowest value: {lowest}")

# Sort the elements in ascending order
ascending_list = sorted(int_list)
print("Sorted in ascending order:")
for num in ascending_list:
    print(num, end=' ')
print()

# Sort the elements in descending order
descending_list = sorted(int_list, reverse=True)
print("Sorted in descending order:")
for num in descending_list:
    print(num, end=' ')
print()

# Append two elements
int_list.append(100)
int_list.append(200)

# Print the list after appending
print("List after appending two elements:")
for num in int_list:
    print(num, end=' ')
print()