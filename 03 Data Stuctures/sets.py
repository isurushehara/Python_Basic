#  Sets in python
#  Sets are unordered collections of unique elements
#  Sets are mutable, meaning you can add or remove elements
#  Sets are defined using curly braces {} or the set() function
#  Sets do not allow duplicate elements
#  Sets are useful for membership testing and eliminating duplicate entries
#  Sets support mathematical operations like union, intersection, difference, and symmetric difference
#  Sets are not indexed, meaning you cannot access elements by their position
#  Sets can only contain immutable (hashable) elements like numbers, strings, and tuples
#  Sets cannot contain mutable elements like lists or dictionaries
#  Sets are implemented using hash tables, which provide average O(1) time complexity for membership tests and insertions
#  Sets are commonly used in scenarios where uniqueness and membership testing are important, such as in data analysis, database operations, and algorithm design

#  Example of creating a set
my_set = {1, 2, 3, 4, 5}
my_set_2 = {4, 5, 6, 7, 8}
my_set_3 = ['a', 'b', 'c', 'd', 'e']

# Example of creating a set using the set() function  
my_set_4 = set(my_set_3)

# Set operations
# Union
union_set = my_set.union(my_set_2)
print("Union:", union_set)
# Pipe operator for union
pipe_union_set = my_set | my_set_2
print("Pipe Union:", pipe_union_set)
# Intersection
intersection_set = my_set.intersection(my_set_2)
print("Intersection:", intersection_set)
# Difference
difference_set = my_set.difference(my_set_2)
print("Difference:", difference_set)
# Pipe operator for union
pipe_union_set = my_set | my_set_2
# Symmetric Difference
symmetric_difference_set = my_set.symmetric_difference(my_set_2)
print("Symmetric Difference:", symmetric_difference_set)

# Add an element to a set
my_set.add(6)
print("After adding 6:", my_set)
# Remove an element from a set
my_set.remove(2)
print("After removing 2:", my_set)

# Search for an element in a set
print("Is 3 in my_set?", 3 in my_set)
print("Is 6 in my_set?", 6 not in my_set)

