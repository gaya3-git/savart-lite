def write_report(profile, result):
    filename = "data/report.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 40 + "\n")
        file.write("SAVART LITE REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Monthly Income   : ₹{profile['monthly_income']}\n")
        file.write(f"Monthly Expenses : ₹{profile['monthly_expenses']}\n")
        file.write(f"Monthly EMI      : ₹{profile['monthly_emi']}\n\n")

        file.write("Scores\n")
        file.write("-" * 40 + "\n")

        file.write(f"Savings Score   : {result['savings']} / 30\n")
        file.write(f"Emergency Score : {result['emergency']} / 25\n")
        file.write(f"Insurance Score : {result['insurance']} / 20\n")
        file.write(f"Debt Score      : {result['debt']} / 25\n\n")

        file.write(f"Total Score : {result['total']}\n")
        file.write(f"Grade       : {result['grade']}\n\n")

        file.write("Recommendations\n")
        file.write("-" * 40 + "\n")

        for recommendation in result["recommendations"]:
            file.write(f"- {recommendation}\n")

    print(f"Report saved successfully: {filename}")