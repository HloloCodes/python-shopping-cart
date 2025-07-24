# tuples
# Tuples are immutable, so you cannot change their elements

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)  # prints (1, 2, 3, 4, 5)

print(my_tuple[0])  # prints 1
print(my_tuple[3])  # prints 4
print(my_tuple[-1])  # prints 5

my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)

conc_tuple = my_tuple1 + my_tuple2  # concatenate tuples
print(conc_tuple)  # prints (1, 2, 3, 4, 5, 6)

rep_tuple = my_tuple1 * 3  # repeat tuple
print(rep_tuple)  # prints (1, 2, 3, 1, 2, 3, 1, 2, 3)

# used for storing fixed data such as coordinates, RGB values, etc.