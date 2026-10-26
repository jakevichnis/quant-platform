from ib_async import Stock

def make_contract(instrument):

    contract = Stock(instrument['symbol'], instrument['exchange'], instrument['currency'])

    return contract