# List in Python
# Like arrays in other languages, but more powerful
# Lists can hold items of different data types, but try to insert same data type element for better performance
# Lists are mutable, meaning you can change their content without changing their identity

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

print("First Elements:", my_list[0])  # Accessing first element
print("Last Element:", my_list[-1])    # Accessing last element

# Elements can be accessed using indexing and slicing
print("Sliced List (2nd to 4th):", my_list[1:4])  # Slicing from index 1 to 3

# Modifying an element
my_list[2] = 10                        
print("After assign [2]th element to 10, Modified List:", my_list)

# Appending elements
my_list.append(6)
print("After append 6, Modified List:", my_list)
# Inserting elements at a specific position
my_list.insert(0, 0)

# Remove elements
my_list.remove(10)  # Remove first occurrence of value 10
print("After remove 10, Modified List:", my_list)
my_list.pop()       # Remove and return the last item
print("After pop(), Modified List:", my_list)

# Add muliple lists
my_list_1 = [7, 8, 9]
my_list_2 = my_list + my_list_1
print("After adding two lists, New List:", my_list_2)

# Length of the list
print("Length of the list:", len(my_list_2))    

# Searching in a list
print("Is 5 in the list?", 5 in my_list_2)  # Check if 5 is in the list
print("Is 5 in the list?", 5 not in my_list_2) # Check if 5 is not in the list
print("Index of 5 in the list:", my_list_2.index(5))  # Get index of first occurrence of 5
print("Count of 5 in the list:", my_list_2.count(5))  # Count occurrences of 5
