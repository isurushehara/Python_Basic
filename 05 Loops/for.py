# For loop in Python
# The for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
# It allows you to execute a block of code multiple times, once for each item in the
# sequence.

# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# You can also use the range() function to generate a sequence of numbers.
# Example:
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# You can specify a start and end value in the range() function.
# Example:
for i in range(1, 3):
    print(i)
# Output:
# 1
# 2

# You can also specify a step value in the range() function.
# Example:
for i in range(0, 10, 2):
    print(i)
# Output:
# 0
# 2
# 4
# 6
# 8

# You can use range() to iterate over the indices of a list.
# Example:
numbers = [1, 2, 3, 4, 5]
range_numbers = range(len(numbers))
for i in range_numbers:
    print(numbers[i])
# Output:
# 1
# 2
# 3
# 4
# 5

# You can use enumerate() funtion
for num in enumerate(numbers):
    print(type(num), num)
# Output:
# <class 'tuple'> (0, 1)
# <class 'tuple'> (1, 2)
# <class 'tuple'> (2, 3)
# <class 'tuple'> (3, 4)
# <class 'tuple'> (4, 5)

for index, value in enumerate(numbers):
    print(index, value)
# Output:
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
