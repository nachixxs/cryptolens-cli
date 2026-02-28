import pytest
from cryptolens.models import CryptoPrice, FearGreedIndex


class TestCryptoPrice:

    def test_is_bullish_positive(self):
        crypto = CryptoPrice("Bitcoin", "BTC", 65000.0, 2.5)
        assert crypto.is_bullish() is True

    def test_is_bullish_negative(self):
        crypto = CryptoPrice("Bitcoin", "BTC", 65000.0, -2.5)
        assert crypto.is_bullish() is False

    @pytest.mark.parametrize("change,expected", [
        (2.35, "▲ 2.35%"),
        (-2.35, "▼ 2.35%"),
        (0.0, "▲ 0.00%"),
    ])
    def test_formatted_change(self, change, expected):
        crypto = CryptoPrice("Bitcoin", "BTC", 65000.0, change)
        assert crypto.formatted_change() == expected


class TestFearGreedIndex:

    def test_sentiment_emoji_extreme_fear(self):
        fg = FearGreedIndex(10, "Extreme Fear", "1709856000")
        assert fg.sentiment_emoji() == "😱"

    def test_sentiment_emoji_greed(self):
        fg = FearGreedIndex(72, "Greed", "1709856000")
        assert fg.sentiment_emoji() == "😊"

    def test_formatted_timestamp(self):
        fg = FearGreedIndex(72, "Greed", "1709856000")
        result = fg.formatted_timestamp()
        assert "/" in result
        assert ":" in result