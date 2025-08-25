# Dictionaries in python
# A dictionary is a collection of key-value pairs
# where each key is unique and maps to a value.
# Dictionaries are mutable, meaning they can be changed after creation.
# They are defined using curly braces {} or the dict() constructor.

# Example of creating a dictionary
my_dict_1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

my_dict_2 = {'22120' : "Pundaluoya", '22121' : "Haputale", '22122' : "Ella"} # Initializing a dictionary with key-value pairs
my_dict_2["22123"] = "Badulla"  # Adding a new key-value pair

# Used keys and paires
print(my_dict_2)
print(my_dict_2.keys())  # Get all keys
print(my_dict_2.values())  # Get all values

x = my_dict_2["22120"] # Accessing a value by its key
x = my_dict_2[0]  # This will raise a KeyError since 0 is not a key in the dictionary
x = my_dict_2.get("22120")  # Using get() to access a value safely
x = my_dict_2.get("22124", "Not Found")  # Providing a default value if the key is not found

# Delete options in dictionaries
del my_dict_2["22120"]  # Deleting a key-value pair by key
my_dict_2.pop("22121")  # Removing a key-value pair and returning its value
my_dict_2.popitem()  # Removing the last inserted key-value pair
my_dict_2.clear()  # Clearing all items in the dictionary
del my_dict_2  # Deleting the entire dictionary