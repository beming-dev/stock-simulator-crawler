# src/main.py

from src.application.news_fetcher import FetchRecentStockNews
from src.infrastructure.database import get_db_connection
from src.repositories.MySQLNewsRepository import MySQLNewsRepository
from src.repositories.MySQLStockRepository import MySQLStockRepository

def main():
    """프로그램의 메인 로직을 실행합니다."""
    conn = get_db_connection()
    
    if conn and conn.is_connected():
        stock_repo = MySQLStockRepository(conn)
        news_repo = MySQLNewsRepository(conn)
        news_fetcher = FetchRecentStockNews(stock_repo, news_repo)
        
        # 임시로 하드코딩된 티커 리스트 사용 (데이터베이스 오류 방지)
        tickers = ["AAPL", "GOOGL", "MSFT", "TSLA"]
        
        conn.close()
        print("데이터베이스 연결이 종료되었습니다.")

        for ticker in tickers:
            news_fetcher.search_google_news_kr(ticker)

if __name__ == "__main__":
    main()