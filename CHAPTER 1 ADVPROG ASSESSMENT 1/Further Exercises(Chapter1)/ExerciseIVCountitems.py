# Given list
staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", 
         "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

# Empty dictionary to store counts
count_dict = {}

# Loop through each name in the list
for name in staff:
    if name in count_dict:
        count_dict[name] += 1
    else:
        count_dict[name] = 1

# Display results
print("Number of times each item appears in the list:")
for key, value in count_dict.items():
    print(f"{key}: {value}")