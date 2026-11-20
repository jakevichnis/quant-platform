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
