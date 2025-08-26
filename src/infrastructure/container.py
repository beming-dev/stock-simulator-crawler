from src.repositories import StockRepository, NewsRepository, MySQLStockRepository, MySQLNewsRepository
from src.application import FetchRecentStockNews
from src.infrastructure import get_db_connection


class DependencyContainer:
    """의존성 주입을 위한 컨테이너 클래스"""
    
    def __init__(self):
        self._db_connection = None
        self._stock_repo = None
        self._news_repo = None
        self._news_fetcher = None
    
    def get_db_connection(self):
        """데이터베이스 연결을 반환합니다 (싱글톤 패턴)"""
        if self._db_connection is None or not self._db_connection.is_connected():
            self._db_connection = get_db_connection()
        return self._db_connection
    
    def get_stock_repository(self) -> StockRepository:
        """StockRepository 인스턴스를 반환합니다"""
        if self._stock_repo is None:
            conn = self.get_db_connection()
            self._stock_repo = MySQLStockRepository(conn)
        return self._stock_repo
    
    def get_news_repository(self) -> NewsRepository:
        """NewsRepository 인스턴스를 반환합니다"""
        if self._news_repo is None:
            conn = self.get_db_connection()
            self._news_repo = MySQLNewsRepository(conn)
        return self._news_repo
    
    def get_news_fetcher(self) -> FetchRecentStockNews:
        """FetchRecentStockNews 인스턴스를 반환합니다"""
        if self._news_fetcher is None:
            stock_repo = self.get_stock_repository()
            news_repo = self.get_news_repository()
            self._news_fetcher = FetchRecentStockNews(stock_repo, news_repo)
        return self._news_fetcher
    
    def cleanup(self):
        """리소스 정리를 수행합니다"""
        if self._db_connection and self._db_connection.is_connected():
            self._db_connection.close()
            print("데이터베이스 연결이 종료되었습니다.")


# 전역 컨테이너 인스턴스
container = DependencyContainer()
