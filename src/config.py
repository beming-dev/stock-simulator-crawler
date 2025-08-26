# src/config.py

import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 불러옵니다.
load_dotenv()

# 데이터베이스 접속 정보를 변수로 저장합니다.
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")