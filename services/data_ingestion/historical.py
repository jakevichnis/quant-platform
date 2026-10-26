


def fetch_history(ib, contract, duration="1 D", bar_size="5 mins"):
    return ib.reqHistoricalData(
        contract,
        endDateTime="",
        durationStr=duration,
        barSizeSetting=bar_size,
        whatToShow="TRADES",
        useRTH=True,
        )