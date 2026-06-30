from savart_lite.inputs import collect_profile

profile = collect_profile()

print(profile)
print("Name:", profile["name"])
print("Age:", profile["age"])
print("Income:", profile["monthly_income"])