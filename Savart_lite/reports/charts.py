import matplotlib

# Use a non-GUI backend so the chart can be saved without opening a window.
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def save_pie_chart(profile):
    income = profile["monthly_income"]
    expenses = profile["monthly_expenses"]
    emi = profile["monthly_emi"]

    savings = income - expenses - emi

    # Avoid negative values if expenses + EMI exceed income
    if savings < 0:
        savings = 0

    labels = ["Expenses", "EMI", "Savings"]
    values = [expenses, emi, savings]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Monthly Income Allocation")

    filename = "data/pie_chart.png"
    plt.savefig(filename)
    plt.close()

    print(f"Pie chart saved successfully: {filename}")

    return filename