from services.data_ingestion.server import DataIngestionServicer, pb

INSTRUMENTS = [{"symbol": "KO"}, {"symbol": "PEP"}]


def test_first_message_is_snapshot():
    servicer = DataIngestionServicer(INSTRUMENTS)
    first = next(servicer.Subscribe(pb.SubscribeRequest(), None))
    assert first.WhichOneof("payload") == "snapshot"
    

def test_snapshot_contains_all_configured_symbols():
    servicer = DataIngestionServicer(INSTRUMENTS)
    first = next(servicer.Subscribe(pb.SubscribeRequest(), None))
    symbols = [t.symbol for t in first.snapshot.ticks]
    assert symbols == ["KO", "PEP"]
    

def test_request_for_first_symbol():
    servicer = DataIngestionServicer(INSTRUMENTS)
    first = next(servicer.Subscribe(pb.SubscribeRequest(symbols=["KO"]), None))
    symbols = [t.symbol for t in first.snapshot.ticks]
    assert symbols == ["KO"]

    