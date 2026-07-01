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

    return breakdown