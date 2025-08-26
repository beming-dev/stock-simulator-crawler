# src/news_fetcher.py

import requests
import xml.etree.ElementTree as ET # XML 파싱을 위한 기본 라이브러리

def search_google_news(ticker):
    """주어진 티커로 구글 뉴스 RSS를 검색하고 기사 제목을 출력합니다."""
    # 검색어에 '주식'을 추가하여 더 정확한 뉴스를 찾습니다. 예: "005930 주식"
    search_query = f"{ticker} 주식"
    url = f"https://news.google.com/rss/search?q={search_query}&hl=ko&gl=KR&ceid=KR:ko"

    print(f"\n--- '{ticker}'에 대한 뉴스 검색 중 ---")

    try:
        response = requests.get(url)
        response.raise_for_status() # HTTP 오류가 발생하면 예외를 발생시킴

        # RSS(XML) 데이터 파싱
        root = ET.fromstring(response.content)

        # <item> 태그 아래의 <title> 태그를 찾아 출력
        news_found = False
        for item in root.findall('.//channel/item'):
            title = item.find('title').text
            print(f"- {title}")
            news_found = True

        if not news_found:
            print("관련 뉴스를 찾을 수 없습니다.")

    except requests.exceptions.RequestException as e:
        print(f"뉴스 요청 중 오류 발생: {e}")
    except ET.ParseError as e:
        print(f"뉴스 데이터 파싱 중 오류 발생: {e}")