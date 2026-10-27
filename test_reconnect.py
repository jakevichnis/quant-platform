import asyncio
from ib_async import IB
from services.data_ingestion.ib_client import (
    reconnect, attach_disconnect_handler, make_reconnect_handler)

async def main():
    ib = IB()
    await reconnect(ib)
    attach_disconnect_handler(ib, make_reconnect_handler(ib, max_attempts=10, base_delay=2))
    print("connected. close TWS, then restart it and log in as Paper")
    await asyncio.sleep(90)
    print("connected:", ib.isConnected())

asyncio.run(main())
