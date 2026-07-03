print("=" * 40)
print("PYTHON FOR LOOPS")
print("=" * 40)

# Basic for loop
print("\n1. Basic for loop")
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# range()
print("\n2. range()")

for i in range(5):
    print(i)

print("\nRange with start and end")

for i in range(1, 6):
    print(i)

print("\nRange with step")

for i in range(0, 11, 2):
    print(i)

# enumerate()
print("\n3. enumerate()")

students = ["Rahul", "Gayathri", "Priya"]

for index, name in enumerate(students):
    print(index, name)

# Nested loops
print("\n4. Nested for loops")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

# break
print("\n5. break")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue
print("\n6. continue")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# pass
print("\n7. pass")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

print("=" * 40)
print("PYTHON WHILE LOOPS")
print("=" * 40)

count = 1

while count <= 5:
    print(count)
    count += 1