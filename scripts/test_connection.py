from ib_async import IB, Stock

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)
print("Connected:", ib.isConnected())

contract = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(contract)

ib.reqMarketDataType(4)  # delayed-frozen: last known delayed values
ticker = ib.reqMktData(contract)
ib.sleep(5)

print(ticker)
print("last:", ticker.last, "| bid:", ticker.bid, "| ask:", ticker.ask, "| close:", ticker.close)

ib.disconnect()


