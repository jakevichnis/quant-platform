import pytest
from services.signal_generation.spread_zscore import zscore


def test_zscore_known_example():
    values = [2, 4, 4, 4, 5, 5, 7, 9]    # 1. set up: input with a known answer
    result = zscore(values)               # 2. call: run your function
    assert result == pytest.approx(2)  # 3. check: the number we worked out by hand