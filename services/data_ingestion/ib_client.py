from ib_async import IB, Stock
import asyncio
import time

def make_contract(instrument):

    contract = Stock(instrument['symbol'], instrument['exchange'], instrument['currency'])

    return contract


def connect(host="127.0.0.1", port=7497, client_id=1):
    ib = IB()
    ib.connect(host, port, clientId=client_id)
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
            if attempt == max_attempts:
                break
            print(f"attempt {attempt} failed ({e}); retrying in {delay}s")
            time.sleep(delay)
    raise ConnectionError(f"could not connect after {max_attempts} attempts")

def attach_disconnect_handler(ib, handler):
    ib.disconnectedEvent += handler



async def reconnect(ib, host="127.0.0.1", port=7497, client_id=1,
                    max_attempts=5, base_delay=1.0):
    for attempt in range(1, max_attempts + 1):
        try:
            await ib.connectAsync(host, port, clientId=client_id)
            return True

        except ConnectionError as e:
            delay = base_delay * (2 ** (attempt - 1))
            print(f"reconnect attempt {attempt} failed ({e})")
            if attempt == max_attempts:
                break
            await asyncio.sleep(delay)
    return False
    