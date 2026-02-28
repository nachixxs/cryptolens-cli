import asyncio
import aiohttp
from cryptolens.fetchers import CoinGeckoFetcher, FearGreedFetcher
from cryptolens.models import MarketReport
from cryptolens.report import print_report


async def main() -> None:
    print("🔍 Obteniendo datos del mercado...")

    coingecko = CoinGeckoFetcher()
    fear_greed = FearGreedFetcher()

    try:
        async with aiohttp.ClientSession() as session:
            prices, fg_index = await asyncio.gather(
                coingecko.fetch(session),
                fear_greed.fetch(session),
            )

        report = MarketReport(prices=prices, fear_greed=fg_index)
        print_report(report)

    except ConnectionError as e:
        print(f"\n❌ Error de conexión:{e}")
    except Exception as e:
        print(f"\n❌ Error inesperado:{e}")


if __name__ == "__main__":
    asyncio.run(main())