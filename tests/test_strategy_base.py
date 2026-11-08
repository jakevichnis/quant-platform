import pytest
from services.signal_generation.strategy_base import Strategy


def test_cannot_instantiate_base():
    with pytest.raises(TypeError):
        Strategy()


def test_complete_subclass_works():
    class Dummy(Strategy):
        def on_tick(self, tick):
            return []

    # create a Dummy, call on_tick(None), assert the result == []
    # setup
    blanker = Dummy()
    # call
    pair_test = blanker.on_tick(None)
    # assert
    assert pair_test == []