import aiohttp
import asyncio
from typing import List
from cryptolens.models import CryptoPrice, FearGreedIndex


COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum,litecoin"
    "&vs_currencies=usd"
    "&include_24hr_change=true"
)
FEAR_GREED_URL = "https://api.alternative.me/fng/?limit=1"
TIMEOUT = aiohttp.ClientTimeout(total=10)


class CoinGeckoFetcher:

    COINS = [
        ("bitcoin", "Bitcoin", "BTC"),
        ("ethereum", "Ethereum", "ETH"),
        ("litecoin", "Litecoin", "LTC"),
    ]

    async def fetch(self, session: aiohttp.ClientSession) -> List[CryptoPrice]:
        try:
            async with session.get(COINGECKO_URL, timeout=TIMEOUT) as response:
                response.raise_for_status()
                data = await response.json()
                return self._parse(data)
        except aiohttp.ClientError as e:
            raise ConnectionError(f"CoinGecko API error: {e}")

    def _parse(self, data: dict) -> List[CryptoPrice]:
        prices = []
        for coin_id, name, symbol in self.COINS:
            coin_data = data[coin_id]
            prices.append(CryptoPrice(
                name=name,
                symbol=symbol,
                price_usd=coin_data["usd"],
                change_24h=coin_data["usd_24h_change"],
            ))
        return prices


class FearGreedFetcher:

    async def fetch(self, session: aiohttp.ClientSession) -> FearGreedIndex:
        try:
            async with session.get(FEAR_GREED_URL, timeout=TIMEOUT) as response:
                response.raise_for_status()
                data = await response.json()
                return self._parse(data)
        except aiohttp.ClientError as e:
            raise ConnectionError(f"Fear & Greed API error: {e}")

    def _parse(self, data: dict) -> FearGreedIndex:
        item = data["data"][0]
        return FearGreedIndex(
            value=int(item["value"]),
            classification=item["value_classification"],
            timestamp=item["timestamp"],
        )