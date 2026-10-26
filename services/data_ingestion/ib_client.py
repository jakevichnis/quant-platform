from ib_async import IB, Stock
import time

def make_contract(instrument):

    contract = Stock(instrument['symbol'], instrument['exchange'], instrument['currency'])

    return contract


def connect(host="127.0.0.1", post=7497, client_id=1):
    ib = IB()
    ib.connect(host, post, clientId=client_id)
    return ib


def connect_with_retry(host="127.0.0.1", port=7497, client_id=1,
                       max_attempts=5, base_delay=1.0):
    ib = IB()
    for attempt in range(1, max_attempts + 1):
        try:
            ib.connect(host, port, clientId=client_id)
            return ib
        except ConnectionError as e:
            delay = base_delay * (2 ** (attempt - 1))
            print(f"attempt {attempt} failed ({e}); retrying in {delay}s")
            time.sleep(delay)
    raise ConnectionError(f"could not connect after {max_attempts} attempts")