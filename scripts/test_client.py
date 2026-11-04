import sys
sys.path.insert(0, "services/data_ingestion")
import grpc
import data_ingestion_pb2 as pb
import data_ingestion_pb2_grpc as pb_grpc

with grpc.insecure_channel("localhost:50051") as channel:
    stub = pb_grpc.DataIngestionStub(channel)
    for update in stub.Subscribe(pb.SubscribeRequest()):
        print(update.WhichOneof("payload"), "->", update)