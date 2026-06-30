def collect_profile():

    name = input("Enter your name: ")

    age = input("Enter your age: ")

    monthly_income = float(input("Monthly Income: "))

    profile = {
        "name": name,
        "age": age,
        "monthly_income": monthly_income
    }

    return profile