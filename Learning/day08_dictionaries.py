print("=" * 40)
print("PYTHON DICTIONARIES")
print("=" * 40)

# Creating a Dictionary
student = {
    "name": "Gayathri",
    "age": 21,
    "branch": "ECE"
}

print("Original Dictionary:")
print(student)

# Accessing values
print("\n1. Accessing Values")
print("Name:", student["name"])
print("Age:", student["age"])

# get()
print("\n2. get()")
print(student.get("branch"))
print(student.get("college", "Key Not Found"))

# keys()
print("\n3. keys()")
print(student.keys())

# values()
print("\n4. values()")
print(student.values())

# items()
print("\n5. items()")
print(student.items())

# update()
print("\n6. update()")
student.update({"age": 22})
print(student)

# setdefault()
print("\n7. setdefault()")
student.setdefault("city", "Chennai")
print(student)

# pop()
print("\n8. pop()")
removed = student.pop("age")
print("Removed:", removed)
print(student)

# popitem()
print("\n9. popitem()")
last_item = student.popitem()
print("Removed:", last_item)
print(student)

# copy()
print("\n10. copy()")
student_copy = student.copy()
print(student_copy)

# clear()
print("\n11. clear()")
temp = student.copy()
temp.clear()
print(temp)

# Looping through Dictionary
print("\n12. Loop through Dictionary")

for key, value in student.items():
    print(key, ":", value)