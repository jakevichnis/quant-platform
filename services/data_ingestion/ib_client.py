from ib_async import IB, Stock

def make_contract(instrument):

    contract = Stock(instrument['symbol'], instrument['exchange'], instrument['currency'])

    return contract


def connect(host="127.0.0.1", post=7497, client_id=1):
    ib = IB()
    ib.connect(host, post, clientId=client_id)
    return ib

