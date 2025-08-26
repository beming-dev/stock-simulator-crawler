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