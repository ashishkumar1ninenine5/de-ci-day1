from src.app.etl import clean_sum


def test_clean_sum_basic():
    assert clean_sum([1, None, 2, 3]) == 6
