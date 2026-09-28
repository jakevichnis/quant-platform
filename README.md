# Quant Trading Platform

Multi-service pairs-trading platform built on Interactive Brokers (paper first).

## Architecture

Signal flow: Data Ingestion → Signal Generation → Risk → Execution → Reconciliation

| Service | Folder | Role |
|---|---|---|
| Data Ingestion | `data_ingestion/` | IB market data (live + historical), served over gRPC |
| Signal Generation | `signal_generation/` | Pluggable strategies emit position intents |
| Risk | `risk/` | Sizing, exposure limits, circuit breakers, VaR |
| Execution | `execution/` | Order placement and state tracking via IB API |
| Reconciliation | `reconciliation/` | Internal vs. IB position checks |
| Backtester | `backtester/` | Validation, slippage/cost model, deflated Sharpe gate |
| Monitoring | `monitoring/` | Structured logging and alerting (cross-cutting) |

Services communicate over gRPC (`.proto` files define each boundary).

## Setup

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

Requires TWS or IB Gateway running in paper mode (TWS paper API port: 7497).