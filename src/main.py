# src/main.py

from src.database import get_db_connection, fetch_stock_tickers
from src.news_fetcher import search_google_news

def main():
    """프로그램의 메인 로직을 실행합니다."""
    # 1. 데이터베이스에 연결
    conn = get_db_connection()

    if conn and conn.is_connected():
        # 2. DB에서 주식 티커 목록 가져오기
        tickers = fetch_stock_tickers(conn)

        # 3. DB 연결 종료
        conn.close()
        print("데이터베이스 연결이 종료되었습니다.")

        # 4. 각 티커에 대해 뉴스 검색 실행
        for ticker in tickers:
            search_google_news(ticker)

if __name__ == "__main__":
    # 이 스크립트가 직접 실행될 때만 main() 함수를 호출
    main()