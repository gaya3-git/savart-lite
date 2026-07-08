def generate_report(profile, result):
    print("\n" + "=" * 40)
    print("        SAVART LITE REPORT")
    print("=" * 40)

    print(f"Monthly Income   : ₹{profile['monthly_income']}")
    print(f"Monthly Expenses : ₹{profile['monthly_expenses']}")
    print(f"Monthly EMI      : ₹{profile['monthly_emi']}")

    print("\nScores")
    print("-" * 40)
    print(f"Savings Score    : {result['savings']} / 30")
    print(f"Emergency Score  : {result['emergency']} / 25")
    print(f"Insurance Score  : {result['insurance']} / 20")
    print(f"Debt Score       : {result['debt']} / 25")

    print("-" * 40)
    print(f"Total Score      : {result['total']}")
    print(f"Grade            : {result['grade']}")

    print("\nRecommendations")
    print("-" * 40)

    for recommendation in result["recommendations"]:
        print(f"• {recommendation}")

    print("=" * 40)