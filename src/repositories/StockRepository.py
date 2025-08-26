from abc import ABC, abstractmethod
from typing import List

from src.domain.entities import Stock


class StockRepository(ABC):
    @abstractmethod
    def fetch_stock_tickers(self) -> List[Stock]:
        pass