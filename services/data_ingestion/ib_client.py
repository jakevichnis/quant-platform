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

        except (ConnectionError, TimeoutError) as e:
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

        except (ConnectionError, TimeoutError) as e:
            delay = base_delay * (2 ** (attempt - 1))
            print(f"reconnect attempt {attempt} failed ({e!r})")
            if attempt == max_attempts:
                break
            await asyncio.sleep(delay)
    return False
    


# Holds references to running reconnect tasks so Python can't garbage-collect them mid-run
_reconnect_tasks = set()


# ================================
def make_reconnect_handler(ib, **kwargs):
    # Closure: the disconnect even passes no arguments, so the handler
    # has to already know which ib to reconnect and with what settings

    def handler():
        print("handler fired")
        task = asyncio.create_task(reconnect(ib, **kwargs))
        # task.add_done_callback(lambda t: print("reconnect task done:", t.exception() or t.result()))
        _reconnect_tasks.add(task)

        def done(t):
            _reconnect_tasks.discard(t)
            if t.cancelled():
                print("reconnect task cancelled")
            elif t.exception():
                print("reconnect fask failed:", repr(t.exception()))
            else:
                print("reconnect task done:", t.result())
        task.add_done_callback(done)
    return handler

# Why a function that returns a function? The event hands the handler no arguments,
# so the handler has to already know which ib to reconnect and with what settings.
# The outer function captures that and builds the right handler for you. This pattern
# is called a closure.

# ==============================