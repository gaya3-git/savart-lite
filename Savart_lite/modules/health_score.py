
from savart_lite.modules.recommendations import generate_recommendations

from savart_lite.modules.savings_ratio import (
    calculate_savings_ratio,
    rate_savings_ratio,
)

from savart_lite.modules.emergency_fund import (
    months_covered,
    fund_status,
)

from savart_lite.modules.insurance import (
    life_cover_adequacy,
)
def calculate_health_score(profile):
    income = profile["monthly_income"]
    expenses = profile["monthly_expenses"]
    emi = profile["monthly_emi"]
    current_savings = profile["current_savings"]
    life_cover = profile["life_insurance_cover"]
    health_insurance = profile["has_health_insurance"]

    breakdown = {
        "savings": 0,
        "emergency": 0,
        "insurance": 0,
        "debt": 0,
    }

    ratio = calculate_savings_ratio(income, expenses)
    saving_status = rate_savings_ratio(ratio)

    months = months_covered(current_savings, expenses)
    emergency_status = fund_status(months)

    insurance_percentage = life_cover_adequacy(life_cover, income)

    # Savings Score
    if saving_status == "Healthy":
        breakdown["savings"] = 30
    elif saving_status == "Average":
        breakdown["savings"] = 15
    else:
        breakdown["savings"] = 0

    # Emergency Fund Score
    if emergency_status == "Healthy":
        breakdown["emergency"] = 25
    elif emergency_status == "Building":
        breakdown["emergency"] = 15
    else:
        breakdown["emergency"] = 0

    # Insurance Score
    if insurance_percentage >= 100:
        breakdown["insurance"] = 20
    elif insurance_percentage >= 60:
        breakdown["insurance"] = 10
    else:
        breakdown["insurance"] = 0

    # Debt Score
    debt_ratio = (emi / income) * 100

    if debt_ratio <= 20:
        breakdown["debt"] = 25
    elif debt_ratio <= 40:
        breakdown["debt"] = 15
    else:
        breakdown["debt"] = 0

    # Total Score
    breakdown["total"] = (
        breakdown["savings"]
        + breakdown["emergency"]
        + breakdown["insurance"]
        + breakdown["debt"]
    )

    # Grade
    if breakdown["total"] >= 80:
        breakdown["grade"] = "A"
    elif breakdown["total"] >= 60:
        breakdown["grade"] = "B"
    elif breakdown["total"] >= 40:
        breakdown["grade"] = "C"
    else:
        breakdown["grade"] = "D"

    # Recommendations
    breakdown["recommendations"] = generate_recommendations(profile, breakdown)

    return breakdown