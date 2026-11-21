from services.signal_generation.strategy_base import Strategy




def decide(z, position, entry=2.0, exit_=0.5):
    """position is None, "SHORT_SPREAD", or "LONG_SPREAD". Returns an action string."""
    if position is None:
        if z > entry:  # price is overinflated, we bet the price goes down
            return "OPEN_SHORT_SPREAD" 
        if z < -entry: # price is severely underpriced, we bet the price will go up
            return "OPEN_LONG_SPREAD"
        return "HOLD"
    if abs(z) > exit_:
        return "CLOSE"
    return "HOLD"

# thoughts on if there's a safeguard where it stays decoupled for too long? or is if that happened that's where we would make a bulk of profit







class PairsStrategy(Strategy):
    strategy_id = "pairs_v1"

    def __init__(self, symbol_a, symbol_b, window=60):
        self.symbol_a = symbol_a
        self.symbol_b = symbol_b
        self.window = window
        self.last = {}          # latest price seen per symbol
        self.history_a = []
        self.history_b = []
        self.position = None    # None, "SHORT_SPREAD", or "LONG_SPREAD"

    def on_tick(self, tick):
        self.last[tick.symbol] = tick.last
        if self.symbol_a not in self.last or self.symbol_b not in self.last:
            return []
        self.history_a.append(self.last[self.symbol_a])
        self.history_b.append(self.last[self.symbol_b])
        if len(self.history_a) < self.window:
            return []
        return []  # signals come in the next piece