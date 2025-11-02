# Outer loop for rows (1 to 5)
for i in range(1, 6):
    # Inner loop for numbers in each row (1 to i)
    for j in range(1, i + 1):
        print(j, end=' ')
    # Print newline after each row
    print()