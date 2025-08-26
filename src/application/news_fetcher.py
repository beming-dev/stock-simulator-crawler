from typing import Dict, List
from src.domain.entities import NewsArticle
from src.repositories import StockRepository
from src.repositories.NewsReposistory import NewsRepository
import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote
from datetime import datetime, timedelta


class FetchRecentStockNews:
    def __init__(self, stock_repo: StockRepository, news_repo: NewsRepository):
        self.stock_repo = stock_repo
        self.news_repo = news_repo

    def search_google_news_kr(self, ticker):
        # 1. 오늘 날짜를 기준으로 이틀 전 날짜를 계산
        two_days_ago = datetime.now() - timedelta(days=2)
        # 2. 'YYYY-MM-DD' 형식으로 변환
        date_str = two_days_ago.strftime('%Y-%m-%d')

        # 3. 검색어에 after: 파라미터를 추가
        search_query = f"{ticker} 주식 after:{date_str}"
        
        encoded_query = quote(search_query)
        url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ko&gl=KR&ceid=KR:ko"

        print(f"\n--- '{ticker}'에 대한 2일 이내 한국어 뉴스 검색 중 (검색어: {search_query}) ---")

        try:
            response = requests.get(url)
            response.raise_for_status()

            root = ET.fromstring(response.content)

            news_found = False
            for item in root.findall('.//channel/item'):
                title = item.find('title').text
                link = item.find('link').text
                pub_date = item.find('pubDate').text
                
                print(f"  - 제목: {title}")
                print(f"  - 링크: {link}")
                print(f"  - 날짜: {pub_date}\n")
                news_found = True

            if not news_found:
                print("최근 2일 내 관련 뉴스를 찾을 수 없습니다.")

        except requests.exceptions.RequestException as e:
            print(f"뉴스 요청 중 오류 발생: {e}")
        except ET.ParseError as e:
            print(f"뉴스 데이터 파싱 중 오류 발생: {e}")


    def search_google_news_en(self, ticker):
        """
        주어진 티커로 미국(영어) 구글 뉴스 RSS를 검색하고,
        '2일 이내'에 게시된 기사의 제목, URL, 날짜를 출력합니다. (after: 쿼리 사용)
        """
        two_days_ago = datetime.now() - timedelta(days=2)
        date_str = two_days_ago.strftime('%Y-%m-%d')

        search_query = f"{ticker} stock after:{date_str}"
        
        encoded_query = quote(search_query)
        url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-US&gl=US&ceid=US:en-US"

        print(f"\n--- '{ticker}'에 대한 2일 이내 영어 뉴스 검색 중 (검색어: {search_query}) ---")

        try:
            response = requests.get(url)
            response.raise_for_status()

            root = ET.fromstring(response.content)

            news_found = False
            for item in root.findall('.//channel/item'):
                title = item.find('title').text
                link = item.find('link').text
                pub_date = item.find('pubDate').text
                
                print(f"  - Title: {title}")
                print(f"  - Link: {link}")
                print(f"  - Date: {pub_date}\n")
                news_found = True

            if not news_found:
                print("No relevant news found within the last 2 days.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the news request: {e}")
        except ET.ParseError as e:
            print(f"An error occurred while parsing news data: {e}")

