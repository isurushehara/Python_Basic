# Tuple in Python
# A tuple is an immutable sequence type in Python, meaning that once it is created, its
# elements cannot be modified, added, or removed.
# Tuples are defined using parentheses () or the tuple() function.
# Tuples can contain elements of different data types, including numbers, strings, lists, and even other tuples.
# Tuples support indexing and slicing, allowing you to access individual elements or sub-tuples.
# Tuples can be nested, meaning you can have tuples within tuples.
# Tuples support various operations such as concatenation, repetition, and membership testing.
# Tuples are often used to group related data together, such as coordinates (x, y) or RGB color values (r, g, b).
# Tuples are more memory efficient than lists, making them a better choice for storing large amounts
# of data that does not need to be modified.
# Tuples can be used as keys in dictionaries because they are immutable, while lists cannot.
# Tuples are commonly used in scenarios where data integrity and immutability are important, such as in
# function arguments, return values, and data structures like sets and dictionaries.

# Example of creating a tuple
my_tuple = ("Isuru", 24, 5.9, True, [1, 2, 3], (4, 5, 6))

# Example of creating a tuple using the tuple() function
my_tuple_2 = tuple([6, 7, 8, 9, 10])

# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slicing from index 1 to 3:", my_tuple[1:4])

# Concatenation of tuples
concatenated_tuple = my_tuple + my_tuple_2
print("Concatenated Tuple:", concatenated_tuple)

# Counting elements in a tuple
count_of_5 = concatenated_tuple.count(5)
print("Count of 5 in concatenated tuple:", count_of_5)

# Expaining elements to variables
name, age, height, is_student, my_list, my_inner_tuple = my_tuple
print("Name:", name)
print("Age:", age)