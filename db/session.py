import os

import asyncpg
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST","localhost")
DB_NAME = os.getenv("DB_NAME","testdb")
DB_USER = os.getenv("DB_USER","postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD","123")
DB_PORT = os.getenv("DB_PORT","5432")

async def create_db_connection() -> asyncpg.Connection:
    try:
        return await asyncpg.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=int(DB_PORT)
        )
    except Exception as e:
        print(f"Database connection occurred :- {str(e)}")
        raise