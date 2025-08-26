# src/database.py

import mysql.connector
from mysql.connector import Error
from src import config # config.py에서 설정 값을 가져옴

def get_db_connection():
    """MySQL 데이터베이스에 연결하고 커넥션 객체를 반환합니다."""
    try:
        conn = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        if conn.is_connected():
            print("데이터베이스에 성공적으로 연결되었습니다.")
            return conn
    except Error as e:
        print(f"데이터베이스 연결 중 오류 발생: {e}")
        return None

def fetch_stock_tickers(conn):
    """DB에서 주식 티커 목록을 가져옵니다."""
    if conn is None:
        return []

    tickers = []
    cursor = conn.cursor() # 쿼리를 실행할 커서 생성

    try:
        # 'stocks' 테이블의 'ticker' 컬럼에서 데이터를 가져온다고 가정
        cursor.execute("SELECT ticker FROM stocks")
        rows = cursor.fetchall() # 모든 결과를 가져옴
        tickers = [row[0] for row in rows] # (('005930',), ('000660',)) -> ['005930', '000660']
        print(f"가져온 티커 목록: {tickers}")
    except Error as e:
        print(f"티커 조회 중 오류 발생: {e}")
    finally:
        cursor.close() # 커서 닫기

    return tickers