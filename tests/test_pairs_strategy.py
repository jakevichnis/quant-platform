from services.signal_generation.pairs_strategy import decide
from types import SimpleNamespace
from services.signal_generation.pairs_strategy import PairsStrategy

def test_high_z_opens_short_spread():
    assert decide(3.0, None) == "OPEN_SHORT_SPREAD"



def make_tick(symbol, last):
    return SimpleNamespace(symbol=symbol, last=last)



def test_no_intents_with_only_one_symbol():
    strategy = PairsStrategy("KO", "PEP", window=3)
    result = strategy.on_tick(make_tick("KO", 92.0))
    assert result == []