from savart_lite.config import LIFE_COVER_INCOME_MULTIPLE

def recommended_life_cover(monthly_income):
    annual_income = monthly_income * 12
    return annual_income * LIFE_COVER_INCOME_MULTIPLE

def life_cover_adequacy(current_cover, monthly_income):
    recommended = recommended_life_cover(monthly_income)

    if recommended <= 0:
        return 0

    return round((current_cover / recommended) * 100, 1)