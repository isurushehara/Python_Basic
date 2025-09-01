# While loop in python
# The while loop is used to execute a block of code as long as a specified condition is true.
# It is useful when you want to repeat a block of code an unknown number of times until
# a certain condition is met.

# Example:
count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0 
# 1
# 2
# 3
# 4
# In this example, the while loop will continue to execute as long as the value of count is less than 5.
# The count variable is incremented by 1 in each iteration, so the loop will eventually
# terminate when count reaches 5.
# Be careful to avoid infinite loops, which occur when the condition never becomes false.

# Example of an infinite loop (commented out to prevent execution):
# while True:
#     print("This will run forever!")

# To break out of a while loop, you can use the break statement.
# Example:
count = 0
while count < 5:
    print(count)
    if count >= 3:
        break
    count += 1  
# Output:
# 0
# 1
# 2
# 3
# In this example, the loop will terminate when count reaches 3 due to the break statement.

# You can also use the continue statement to skip the current iteration and move to the next one.
# Example:
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
# Output:
# 1
# 2
# 4
# 5
# In this example, when count is 3, the continue statement will skip the print statement
# and move to the next iteration of the loop.
