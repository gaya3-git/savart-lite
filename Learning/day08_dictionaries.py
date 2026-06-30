# day08_dictionaries.py

# Learning Python Dictionaries.

expenses = {
    "rent": 12000,
    "food": 8000,
    "transport": 4500
}

print(expenses)

print("Rent is Rs.", expenses["rent"])

expenses["fun"] = 3000
expenses["food"] = 8500

print(expenses)

total = 0

for category, amount in expenses.items():
    print(category, "-> Rs.", amount)
    total = total + amount

print("Total: Rs.", total)

# Safe access using get()
print("Insurance:", expenses.get("insurance", 0))
print("Rent:", expenses.get("rent", 0))

student = {
    "name": "Gayathri",
    "age": 20,
    "branch": "ECE"
}
student["cgpa"] = 7.5
student.get("college", "Not Available")