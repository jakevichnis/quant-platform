import os
import sys
import time
from concurrent import futures
sys.path.insert(0, os.path.dirname(__file__))

import grpc
import data_ingestion_pb2 as pb
import data_ingestion_pb2_grpc as pb_grpc

PORT = 50051

class DataIngestionServicer(pb_grpc.DataIngestionServicer):
    def __init__(self, instruments):
        self.symbols = [i["symbol"] for i in instruments]
    def Subscribe(self, request, context):
        wanted = list(request.symbols) or self.symbols

        # 1. snapshot first: latest state of every instrument
        now = int(time.time() * 1000)
        ticks = [pb.Tick(symbol=s, bid=100.0, ask=100.02, last=100.01, timestamp_ms=now)
                 for s in wanted]
        yield pb.MarketDataUpdate(snapshot=pb.Snapshot(ticks=ticks))

        # 2. then one tick at a time (5 rounds, 1 second apart)

        for round_number in range(5):
            time.sleep(1)
            for s in wanted:
                tick = pb.Tick(symbol=s, bid=100.0, ask=100.02, last=100.01,
                               timestamp_ms=int(time.time() * 1000))
                yield pb.MarketDataUpdate(tick=tick)
        


def serve(instruments, port=PORT):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    pb_grpc.add_DataIngestionServicer_to_server(DataIngestionServicer(instruments), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    return server


if __name__ == "__main__":
    from services.data_ingestion.config import load_instruments
    server = serve(load_instruments("config/instruments.yaml"))
    print(f"data ingestion server listening on {PORT}")
    server.wait_for_termination()



