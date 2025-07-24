# Sets
# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements.
# Sets are useful for storing unique items and performing set operations like union, intersection, and difference.
# Sets do not support indexing or slicing, as they are unordered.

my_set = {1, 2, 3, 4, 5}
print(my_set)  # prints {1, 2, 3, 4, 5}

my_set.add(6)  # add an element
print(my_set)  # prints {1, 2, 3, 4, 5, 6}

my_set.remove(3)  # remove an element
print(my_set)  # prints {1, 2, 4, 5,

my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5, 6}

# Union
union_set = my_set1.union(my_set2)  # union of two sets
print(union_set)  # prints {1, 2, 3, 4, 5, 6}

# Intersection
inter_set = my_set1.intersection(my_set2)  # intersection of two sets
print(inter_set)  # prints {3}

#Difference
diff_set = my_set1.difference(my_set2)  # difference of two sets
print(diff_set)  # prints {1, 2}


