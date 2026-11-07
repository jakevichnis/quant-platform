from abc import ABC, abstractmethod

class Strategy(ABC):
    strategy_id = "base"

    @abstractmethod
    def on_tick(self, tick):
        """Receive one market data Tick. Return a list of PositionIntent (may be empty)."""

        