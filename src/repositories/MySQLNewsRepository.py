from typing import List
from mysql.connector.connection import MySQLConnection
from src.domain.entities import NewsArticle
from src.repositories.NewsRepository import NewsRepository


class MySQLNewsRepository(NewsRepository):
    def __init__(self, conn: MySQLConnection):
        self.conn = conn

    def save_news_article(self, article: NewsArticle) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO news_articles (title, link, pub_date) VALUES (%s, %s, %s)",
                (article.title, article.link, article.pub_date)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"뉴스 기사 저장 중 오류 발생: {e}")
            return False

    def get_news_by_ticker(self, ticker: str) -> List[NewsArticle]:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT title, link, pub_date FROM news_articles WHERE title LIKE %s",
                (f"%{ticker}%",)
            )
            rows = cursor.fetchall()
            return [NewsArticle(title=row[0], link=row[1], pub_date=row[2]) for row in rows]
        except Exception as e:
            print(f"뉴스 기사 조회 중 오류 발생: {e}")
            return []
