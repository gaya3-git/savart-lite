from savart_lite.config import (
    EMERGENCY_FUND_TARGET_MONTHS,
    EMERGENCY_FUND_OK_MONTHS
)

def months_covered(current_savings, monthly_expenses):
    if monthly_expenses <= 0:
        return 0.0

    return round(current_savings / monthly_expenses, 1)


def target_amount(monthly_expenses):
    return EMERGENCY_FUND_TARGET_MONTHS * monthly_expenses


def fund_status(months):
    if months >= EMERGENCY_FUND_TARGET_MONTHS:
        return "Healthy"
    elif months >= EMERGENCY_FUND_OK_MONTHS:
        return "Building"
    else:
        return "Critical"