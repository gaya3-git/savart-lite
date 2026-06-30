# day09_functions.py
# A function is a reusable block of code with a name. I package the
# savings-ratio maths into one function so I can call it many times.
def savings_ratio(income, expenses):
 """Return the savings ratio as a percentage, rounded to 1 decimal."""
 # income and expenses are "parameters": values passed in at call time.
 surplus = income - expenses
 ratio = (surplus / income) * 100
 return round(ratio, 1) # return = hand the answer back to the
caller
# Call the function with different numbers (the whole point of a function:
# write once, reuse many times).
print("Asha:", savings_ratio(50000, 32000), "%")
print("Ravi:", savings_ratio(80000, 60000), "%")