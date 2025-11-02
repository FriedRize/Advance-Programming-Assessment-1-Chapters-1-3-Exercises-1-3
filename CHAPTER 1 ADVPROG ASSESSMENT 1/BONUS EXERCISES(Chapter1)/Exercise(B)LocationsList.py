# Given list
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

# 1. Print the list and find the length of the list
print("Original list:", locations)
print("Length of the list:", len(locations))

# 2. Use sorted() to print list in alphabetical order (without modifying original)
print("\nList in alphabetical order using sorted():", sorted(locations, key=str.lower))

# 3. Show that the list is still in original order
print("List after using sorted() (original order):", locations)

# 4. Use sorted() to print list in reverse alphabetical order (without modifying original)
print("\nList in reverse alphabetical order using sorted():", sorted(locations, key=str.lower, reverse=True))

# 5. Show that the list is still in original order
print("List after using sorted() in reverse (original order):", locations)

# 6. Use reverse() to change the order of the list
locations.reverse()
print("\nList after using reverse():", locations)

# 7. Use sort() to store list in alphabetical order
locations.sort(key=str.lower)
print("List after using sort() (alphabetical order):", locations)

# 8. Use sort() to store list in reverse alphabetical order
locations.sort(key=str.lower, reverse=True)
print("List after using sort() (reverse alphabetical order):", locations)