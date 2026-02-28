import pytest
from cryptolens.fetchers import CoinGeckoFetcher, FearGreedFetcher
from cryptolens.models import CryptoPrice, FearGreedIndex


MOCK_COINGECKO_RESPONSE = {
    "bitcoin": {"usd": 65420.0, "usd_24h_change": -2.35},
    "ethereum": {"usd": 3210.5, "usd_24h_change": 1.12},
    "litecoin": {"usd": 87.3, "usd_24h_change": 0.45},
}

MOCK_FEAR_GREED_RESPONSE = {
    "data": [{"value": "72", "value_classification": "Greed", "timestamp": "1709856000"}]
}


class TestCoinGeckoFetcher:

    def test_parse_returns_three_prices(self):
        fetcher = CoinGeckoFetcher()
        result = fetcher._parse(MOCK_COINGECKO_RESPONSE)
        assert len(result) == 3

    def test_parse_bitcoin_price(self):
        fetcher = CoinGeckoFetcher()
        result = fetcher._parse(MOCK_COINGECKO_RESPONSE)
        btc = result[0]
        assert btc.symbol == "BTC"
        assert btc.price_usd == 65420.0
        assert btc.change_24h == -2.35

    def test_parse_returns_crypto_price_instances(self):
        fetcher = CoinGeckoFetcher()
        result = fetcher._parse(MOCK_COINGECKO_RESPONSE)
        assert all(isinstance(item, CryptoPrice) for item in result)


class TestFearGreedFetcher:

    def test_parse_returns_fear_greed_index(self):
        fetcher = FearGreedFetcher()
        result = fetcher._parse(MOCK_FEAR_GREED_RESPONSE)
        assert isinstance(result, FearGreedIndex)

    def test_parse_value(self):
        fetcher = FearGreedFetcher()
        result = fetcher._parse(MOCK_FEAR_GREED_RESPONSE)
        assert result.value == 72
        assert result.classification == "Greed"