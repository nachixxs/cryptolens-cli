# CryptoLens CLI

> Archived: learning project, no longer maintained.

Small async command-line tool that prints a one-shot crypto market report: current USD price and 24h change for BTC, ETH and LTC from the CoinGecko API, plus the Fear & Greed Index from alternative.me. Both requests run concurrently with `asyncio.gather()` over a shared `aiohttp` session. No API keys needed. Console messages are in Spanish.

It was my exercise in asyncio and dataclasses, and the starting point for [crypto-market-api](https://github.com/nachixxs/crypto-market-api).

## Run

```bash
python -m venv venv
venv\Scripts\activate    # Windows; use source venv/bin/activate elsewhere
pip install -r requirements.txt
python main.py
```

## Structure

```
cryptolens/
  models.py     # dataclasses: CryptoPrice, FearGreedIndex, MarketReport
  fetchers.py   # async fetchers for CoinGecko and Fear & Greed, with a 10 s timeout
  report.py     # console output
tests/          # 11 pytest tests on models and response parsing (no network)
main.py
```

Run the tests with `pytest tests/ -v`.
