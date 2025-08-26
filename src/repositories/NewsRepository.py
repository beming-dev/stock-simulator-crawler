from abc import ABC, abstractmethod
from typing import List

from src.domain.entities import NewsArticle


class NewsRepository(ABC):
    @abstractmethod
    def save_news_article(self, article: NewsArticle) -> bool:
        pass
    
    @abstractmethod
    def get_news_by_ticker(self, ticker: str) -> List[NewsArticle]:
        pass