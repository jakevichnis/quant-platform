import numpy as np
import pytest
from services.signal_generation.cointegration import hedge_ratio, spread, check_pair


def make_pair():
    rng = np.random.default_rng(0)
    b = np.cumsum(rng.normal(size=500)) + 100
    a = 2.8 * b + rng.normal(scale=0.5, size=500)
    return a, b


def test_hedge_ratio_is_about_2_8():
    a, b = make_pair()
    ratio = hedge_ratio(a, b)
    assert ratio == pytest.approx(2.8, abs=0.05)


def test_check_pair_finds_the_leash():
    a, b = make_pair()
    ok, p = check_pair(a, b)
    assert ok

