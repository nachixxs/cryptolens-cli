from cryptolens.models import MarketReport


def print_report(report: MarketReport) -> None:
    _print_header(report.fetched_at)
    _print_prices(report)
    _print_fear_greed(report)
    _print_footer()


def _print_header(fetched_at: str) -> None:
    print("\n" + "═" * 45)
    print("       🔍 CryptoLens — Market Report")
    print(f"       📅{fetched_at}")
    print("═" * 45)


def _print_prices(report: MarketReport) -> None:
    print("\n  💰 CRYPTO PRICES\n")
    for crypto in report.prices:
        change = crypto.formatted_change()
        print(f"  {crypto.symbol:<6} ${crypto.price_usd:>12,.2f}     {change}")


def _print_fear_greed(report: MarketReport) -> None:
    fg = report.fear_greed
    emoji = fg.sentiment_emoji()
    print("\n" + "─" * 45)
    print(f"\n{emoji}  FEAR & GREED INDEX\n")
    print(f"  Value:{fg.value}/100")
    print(f"  Mood:{fg.classification}")
    print(f"  As of:{fg.formatted_timestamp()}")


def _print_footer() -> None:
    print("\n" + "═" * 45)
    print("  Data: CoinGecko · alternative.me")
    print("═" * 45 + "\n")