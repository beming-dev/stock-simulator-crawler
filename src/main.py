# src/main.py

from src.infrastructure import container

def main():
    """프로그램의 메인 로직을 실행합니다."""
    try:
        # 의존성 주입 컨테이너에서 필요한 객체들을 가져옴
        news_fetcher = container.get_news_fetcher()
        
        # 임시로 하드코딩된 티커 리스트 사용 (데이터베이스 오류 방지)
        tickers = ["AAPL", "GOOGL", "MSFT", "TSLA"]
        
        # 각 티커에 대해 뉴스 검색 수행
        for ticker in tickers:
            news_fetcher.search_google_news_kr(ticker)
            
    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")
    finally:
        # 리소스 정리
        container.cleanup()

if __name__ == "__main__":
    main()