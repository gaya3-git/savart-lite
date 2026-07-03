# ============================
# PYTHON LISTS
# ============================

# Creating a List
fruits = ["Apple", "Banana", "Orange"]
print("Original List:", fruits)

# append() - Adds one item at the end
fruits.append("Mango")
print("append():", fruits)

# extend() - Adds multiple items
fruits.extend(["Grapes", "Pineapple"])
print("extend():", fruits)

# insert() - Inserts item at a specific position
fruits.insert(1, "Kiwi")
print("insert():", fruits)

# remove() - Removes a specific item
fruits.remove("Orange")
print("remove():", fruits)

# pop() - Removes item by index
removed_item = fruits.pop(2)
print("pop():", fruits)
print("Removed Item:", removed_item)

# index() - Returns index of an item
print("index():", fruits.index("Kiwi"))

# count() - Counts occurrences
numbers = [1, 2, 3, 2, 2, 5]
print("count():", numbers.count(2))

# sort() - Sorts list
numbers.sort()
print("sort():", numbers)

# reverse() - Reverses list
numbers.reverse()
print("reverse():", numbers)

# copy() - Creates a copy
copy_list = fruits.copy()
print("copy():", copy_list)

# clear() - Removes all items
temp = [10, 20, 30]
temp.clear()
print("clear():", temp)

# len() - Returns length
print("len():", len(fruits))

print("\n==============================")
print("PYTHON TUPLES")
print("==============================")

# Creating Tuple
tuple_data = (10, 20, 30, 20)

print("Tuple:", tuple_data)
print("Length:", len(tuple_data))
print("Index of 30:", tuple_data.index(30))
print("Count of 20:", tuple_data.count(20))

print("\n==============================")
print("PYTHON SETS")
print("==============================")

colors = {"Red", "Green", "Blue"}

print("Original Set:", colors)

# add()
colors.add("Yellow")
print("add():", colors)

# update()
colors.update({"Black", "White"})
print("update():", colors)

# remove()
colors.remove("Green")
print("remove():", colors)

# discard()
colors.discard("Pink")
print("discard():", colors)

# pop()
removed = colors.pop()
print("pop():", colors)
print("Removed:", removed)

# clear()
sample = {"A", "B"}
sample.clear()
print("clear():", sample)