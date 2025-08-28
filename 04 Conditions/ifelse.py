# Conditions in Python

# If Statements
# The if statement is used to test a specific condition.
# If the condition is true, the block of code inside the if statement is executed.
# Example:
age = 18
if age >= 18:
    print("You are an adult.") # Output: You are an adult.

# You can also use logical operators (and, or, not) to combine multiple conditions.
# Example:
age = 20
if age >= 18 and age < 65:
    print("You are an adult but not a senior citizen.") # Output: You are an adult but not a senior citizen.
if age < 18 or age >= 65:
    print("You are either a minor or a senior citizen.")

# If-Else Statements
# The if-else statement is used to execute one block of code if the condition is true,
# and another block of code if the condition is false.
# Example:
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.") # Output: You are a minor.

# If-Elif-Else Statements
# The if-elif-else statement is used to test multiple conditions.
# The first block of code with a true condition is executed.
# If none of the conditions are true, the else block is executed.
# Example:
score = 70
if score >= 75 and score <= 100:
    print("Grade: A")
elif score >= 65 and score < 75:
    print("Grade: B") # Output: Grade: B
elif score >= 55 and score < 65:
    print("Grade: C")
elif score >= 35 and score < 55:
    print("Grade: S")
elif score >= 0 and score < 35:
    print("Grade: F")
else:
    print("Invalid score")

# Nested If Statements
# You can also nest if statements inside other if statements.
# Example:
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.") # Output: The number is positive and even.
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

# Note: Indentation is crucial in Python to define the scope of the blocks of code.
# Make sure to use consistent indentation (usually 4 spaces) for nested blocks.

# If-Else as a One-Liner
# You can also write if-else statements in a single line using the ternary operator.
age = 20
status = "Adult" if age >= 18 else "Minor"