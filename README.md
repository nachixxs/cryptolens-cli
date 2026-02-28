# 🔍 CryptoLens CLI

> Real-time crypto market snapshot from the command line.

Fetches Bitcoin, Ethereum and Litecoin prices alongside the Fear & Greed Index
and displays a consolidated market report in seconds.

## Features

-⚡ Concurrent API calls with `asyncio.gather()` — no waiting one by one
-💰 Live prices + 24h change for BTC, ETH and LTC (CoinGecko)
-🧠 Market sentiment index 0-100 (Fear & Greed Index)
-✅ Fully tested with pytest — no internet required to run tests
-🔑 No API keys needed — clone and run immediately

## Installation

```bash
git clone https://github.com/nachixxs/cryptolens-cli.git
cd cryptolens-cli
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Run tests

```bash
pytest tests/ -v
```

## Tech stack

| Tool | Purpose |
|---|---|
| `asyncio` + `aiohttp` | Concurrent HTTP requests |
| `dataclasses` | Typed data models |
| `pytest` | Testing without internet dependency |

## Project structure

```
cryptolens-cli/
├── cryptolens/
│   ├── models.py      # Dataclasses
│   ├── fetchers.py    # Async API calls
│   └── report.py      # Console output
├── tests/
│   ├── test_models.py
│   └── test_fetchers.py
├── main.py
└── requirements.txt
```

## Author

**Nacho Noguerol**
[GitHub](https://github.com/nachixxs) · [LinkedIn](https://www.linkedin.com/in/ignacio-noguerol-54aa942b0/) · ignacionogpa@gmail.com
