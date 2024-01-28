import pytest
from src.roller_coaster import height_checker

@pytest.mark.parametrize("height, expected", [
    (119, False),  # 120cm未満
    (120, True),   # 120cm境界値
    (169, True),   # 170cm未満
    (170, False)   # 170cm境界値
])
def test_height_checker(height, expected):
    assert height_checker(height) == expected