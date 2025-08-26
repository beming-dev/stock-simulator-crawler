
from datetime import datetime


class NewsArticle:
    def __init__(self, title: str, link: str, pub_date: datetime):
        self.title = title
        self.link = link
        self.pub_date = pub_date