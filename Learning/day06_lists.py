# day06_lists.py

# Learning Python Lists.

expenses = [12000, 8000, 4500, 3000]

print(expenses)

print("First expense:", expenses[0])
print("Second expense:", expenses[1])
print("Third expense:", expenses[2])
print("Fourth expense:", expenses[3])

print("Number of expenses:", len(expenses))

expenses.append(2500)

print(expenses)

total_expense = sum(expenses)

print("Total Expense:", total_expense)

print("Highest Expense:", max(expenses))
print("Lowest Expense:", min(expenses))