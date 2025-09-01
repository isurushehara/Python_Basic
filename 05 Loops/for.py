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

# For loop with break 
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2
# In this example, the loop will terminate when i reaches 3 due to the break statement.

# For loop with continue
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output:
# 0
# 1
# 2
# 4
# In this example, when i is 3, the continue statement will skip the print statement
# and move to the next iteration of the loop.

# You can also use the else statement with a for loop.
# The else block will be executed when the loop is finished, unless it is terminated by a break statement.
# Example:
for i in range(5):
    print(i)
else:
    print("Loop is finished")
# Output:
# 0
# 1
# 2
# 3
# 4
# Loop is finished
# In this example, the else block will be executed after the loop is finished.

# If the loop is terminated by a break statement, the else block will not be executed.
# Example:
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop is finished")
# Output:
# 0
# 1
# 2
# In this example, the else block will not be executed because the loop is terminated by a break statement.

# You can also use for loops to iterate dictionaries.
# Example:
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, person[key])

# Or
# for key, value in person.items():
#     print(key, value)
# Output:
# name John
# age 30
# city New York
# In this example, the for loop iterates over the keys of the dictionary and prints each key along with its corresponding value.

# You can use for loops to irerate over strings.
# Example:
for char in "Hello":
    print(char)
# Output:
# H
# e
# l
# l
# o
# In this example, the for loop iterates over each character in the string "Hello" and prints it.

# You can use for loops for iterate a set.
# Example:
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
# Output:
# 1
# 2
# 3
# 4
# 5
# In this example, the for loop iterates over each item in the set and prints it.

# You can use for loops to iterate over tuples.
# Example:
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3
# 4
# 5
# In this example, the for loop iterates over each item in the tuple and prints it.

# You can also use nested for loops to iterate over multi-dimensional data structures.
# Example:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # for new line after each row 
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
# In this example, the outer for loop iterates over each row of the matrix,
# and the inner for loop iterates over each element in the current row.
# The end=" " parameter in the print function is used to print elements in the same line separated by a space.
# This is a basic overview of for loops in Python. They are a powerful tool for iterating over sequences and performing repetitive tasks.
