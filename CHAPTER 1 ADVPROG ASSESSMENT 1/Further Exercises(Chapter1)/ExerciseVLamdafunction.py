# Given list of marks
marks = [("CodeLab I", 67), 
         ("Web Development", 75), 
         ("CodeLab II", 74), 
         ("Smartphone Apps", 68), 
         ("Games Development", 70), 
         ("Responsive Web", 65)]

# Sort low to high
low_to_high = sorted(marks, key=lambda x: x[1])
print("Marks sorted from low to high:")
for subject, mark in low_to_high:
    print(f"{subject}: {mark}")

print()  # Blank line

# Sort high to low
high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)
print("Marks sorted from high to low:")
for subject, mark in high_to_low:
    print(f"{subject}: {mark}")