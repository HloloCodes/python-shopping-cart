# Dictionary
# are used to store data values in key:value pairs.
# They are mutable, meaning you can change their content.
# Dictionaries are unordered, meaning the items have no index.
# They are useful for storing data that is related, like a person's details (name, age, address).

my_dict = { "apple": 1, "banana": 2, "cherry": 3 }

print(my_dict)  # prints {'apple': 1, 'banana': 2, 'cherry': 3}
print(my_dict["apple"])  # prints 1

my_dict["grapes"] = 5  #  add a new key-value pair
print(my_dict)  # prints {'apple': 1, 'banana': 2, 'cherry': 3, 'grapes': 5}

my_dict["banana"] = 4  # change the value of an existing key
print(my_dict)  # prints {'apple': 1, 'banana': 4, 'cherry': 3, 'grapes': 5}