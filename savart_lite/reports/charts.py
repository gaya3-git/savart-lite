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


def save_bar_chart(result):
    labels = ["Savings", "Emergency", "Insurance", "Debt"]
    scores = [
        result["savings"],
        result["emergency"],
        result["insurance"],
        result["debt"],
    ]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, scores)

    plt.title("Financial Health Score Breakdown")
    plt.xlabel("Categories")
    plt.ylabel("Score")

    filename = "data/bar_chart.png"
    plt.savefig(filename)
    plt.close()

    print(f"Bar chart saved successfully: {filename}")

    return filename