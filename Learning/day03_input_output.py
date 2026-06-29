# day03_input_output.py
# Learning input and output in Python.
name = input("What is your name? ")
income = float(input("What is your monthly income (Rs.)? "))
expenses = float(input("What are your monthly expenses (Rs.)? "))
print(name)
print(income)
print(expenses)
savings = income - expenses
print("Savings:", savings)
print(name, "saves Rs.", savings, "every month.")