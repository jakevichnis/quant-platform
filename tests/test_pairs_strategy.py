from services.signal_generation.pairs_strategy import decide


def test_high_z_opens_short_spread():
    assert decide(3.0, None) == "OPEN_SHORT_SPREAD"