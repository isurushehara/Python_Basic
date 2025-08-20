# Type Conversion in Python
# print("\nType Conversion:")

# To Integer
number = "42"
integer_number = int(number)  # Convert string to integer

# To String
number = 42
string_number = str(number)  # Convert integer to string

#To Boolean
result = "True"
boolean_result = bool(result)  # Convert string to boolean

# Get input from user (always get as a string)
num1, num2 = input("Enter first number: "), input("Enter second number: ")
print("Sum of", num1, "and", num2, "is:", int(num1) + int(num2))  # Convert to integer and add
