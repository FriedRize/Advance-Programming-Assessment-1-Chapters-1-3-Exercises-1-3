for i in range(1, 11):  # Outer loop for each table
    print(f"Multiplication table of : {i}")
    for j in range(1, 11):  # Inner loop for each multiplier
        print(f"{i} x {j} = {i * j}")
    print()  # Blank line between tables for better readability