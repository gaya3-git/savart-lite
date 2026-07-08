def collect_profile():

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    monthly_income = float(input("Monthly Income: "))
    monthly_expenses = float(input("Monthly Expenses: "))
    monthly_emi = float(input("Monthly EMI: "))
    current_savings = float(input("Current Savings: "))
    life_insurance_cover = float(input("Life Insurance Cover: "))

    health = input("Do you have Health Insurance? (yes/no): ").lower()

    has_health_insurance = health == "yes"

    profile = {
        "name": name,
        "age": age,
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "monthly_emi": monthly_emi,
        "current_savings": current_savings,
        "life_insurance_cover": life_insurance_cover,
        "has_health_insurance": has_health_insurance,
    }

    return profile