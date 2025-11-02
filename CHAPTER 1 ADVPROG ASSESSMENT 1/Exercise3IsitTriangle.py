# Function to check if three sides can form a triangle
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Function to classify the triangle
def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"

# Main program
print("Enter the lengths of the three sides of a triangle:")
print("Side 1:")
side1 = float(input())
print("Side 2:")
side2 = float(input())
print("Side 3:")
side3 = float(input())

# Check if sides are positive
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Invalid input: All side lengths must be positive numbers.")
else:
    # Check triangle inequality
    if is_valid_triangle(side1, side2, side3):
        triangle_type = classify_triangle(side1, side2, side3)
        print(f"The sides {side1}, {side2}, {side3} can form a triangle.")
        print(f"It is a {triangle_type} triangle.")
    else:
        print(f"The sides {side1}, {side2}, {side3} cannot form a triangle.")