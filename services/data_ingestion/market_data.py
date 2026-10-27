


def subscribe(ib, contracts, on_tickers):
    ib.reqMarketDataType(3)     # 3 = delayed data
    tickers = [ib.reqMktData(c) for c in contracts]
    ib.pendingTickersEvent += on_tickers
    return tickers

