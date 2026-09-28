from ib_insync import IB, Stock

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

print("Connected:", ib.isConnected())

contract = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(contract)
ticker = ib.reqMktData(contract)
ib.sleep(2)
print("AAPL last price:", ticker.last)

ib.disconnect()