# Function to calculate the product of all elements in a list
def list_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Main program
# Example list
my_list = [2, 3, 4, 5]

# Calling the function and storing the result
result = list_product(my_list)

# Displaying the result
print("The list is:", my_list)
print("The product of the list values is:", result)