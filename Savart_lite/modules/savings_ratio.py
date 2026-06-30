from savart_lite.config import SAVINGS_RATIO_HEALTHY, SAVINGS_RATIO_OK


def calculate_savings_ratio(income, expenses):
    """Return savings ratio as a percentage rounded to 1 decimal."""

    if income <= 0:
        raise ValueError("Income must be greater than zero.")

    surplus = income - expenses
    return round((surplus / income) * 100, 1)


def rate_savings_ratio(ratio):
    """Return a friendly label for the savings ratio."""

    if ratio >= SAVINGS_RATIO_HEALTHY:
        return "Healthy"
    elif ratio >= SAVINGS_RATIO_OK:
        return "Average"
    else:
        return "Poor"