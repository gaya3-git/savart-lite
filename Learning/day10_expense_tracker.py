# day10_expense_tracker.py

# Mini Project - Expense Tracker

expenses = []

def add_expense():
    name = input("Expense Name: ")
    amount = float(input("Amount (Rs.): "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

def view_expenses():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for expense in expenses:
        print(expense)

def show_total():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense: Rs.", total)

while True:

    print("\n======================")
    print("Expense Tracker")
    print("======================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Please try again.")