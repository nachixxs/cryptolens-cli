from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass
class CryptoPrice:
    name: str
    symbol: str
    price_usd: float
    change_24h: float

    def is_bullish(self) -> bool:
        return self.change_24h > 0

    def formatted_change(self) -> str:
        arrow = "▲" if self.is_bullish() else "▼"
        return f"{arrow}  {abs(self.change_24h):.2f}%"


@dataclass
class FearGreedIndex:
    value: int
    classification: str
    timestamp: str

    def formatted_timestamp(self) -> str:
        dt = datetime.fromtimestamp(int(self.timestamp))
        return dt.strftime("%d/%m/%Y %H:%M")

    def sentiment_emoji(self) -> str:
        if self.value <= 25:
            return "😱"
        elif self.value <= 45:
            return "😰"
        elif self.value <= 55:
            return "😐"
        elif self.value <= 75:
            return "😊"
        else:
            return "🤑"


@dataclass
class MarketReport:
    prices: List[CryptoPrice]
    fear_greed: FearGreedIndex
    fetched_at: str = field(default_factory=lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S"))