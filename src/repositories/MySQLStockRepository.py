from typing import List
from mysql.connector.connection import MySQLConnection
from src.domain.entities import Stock
from src.repositories import StockRepository


class MySQLStockRepository(StockRepository):
    def __init__(self, conn: MySQLConnection):
        self.conn = conn

    def get_all_tickers(self) -> List[str]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT ticker FROM stock")
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def fetch_stock_tickers(self) -> List[Stock]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT ticker, name FROM stock")
        rows = cursor.fetchall()
        return [Stock(ticker=row[0], name=row[1]) for row in rows]