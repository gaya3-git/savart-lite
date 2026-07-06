from savart_lite.modules.savings_ratio import calculate_savings_ratio
from savart_lite.modules.emergency_fund import months_covered
from savart_lite.modules.insurance import life_cover_adequacy


def test_savings_ratio():
    assert calculate_savings_ratio(50000, 30000) == 40.0


def test_emergency_fund():
    assert months_covered(180000, 30000) == 6.0


def test_insurance():
    assert life_cover_adequacy(500000, 50000) == 83.33