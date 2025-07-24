fruits = ["apples", "bananas", "cherries"]
print(fruits[0])  # prints "apples"
print(fruits[1])  # prints "bananas"

fruits[1] = "blueberries"  # change "bananas" to "blueberries"
print(fruits)  # prints ["apples", "blueberries", "cherries"]

fruits.append("kiwi") # add "kiwi" to the end of the list
print(fruits)

fruits.insert(1, "mango")  # insert "mango" at index 1
print(fruits)  # prints ["apples", "mango", "blueberries"]

fruits.remove("kiwi")  # remove "kiwi"
print(fruits)

fruits.sort()  # sort the list in alphabetical order
print(fruits)

fruits.sort(reverse=True)  # sort the list in reverse alphabetical order
print(fruits)