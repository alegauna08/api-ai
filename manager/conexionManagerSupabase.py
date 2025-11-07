import os
from typing import Generator

import psycopg
from dotenv import load_dotenv

load_dotenv()
passwordDB = os.getenv("SUPABASE_PASSWORD")
url = f"postgresql://postgres.bngqmlgvlqwvvxwculhn:{passwordDB}@aws-1-us-east-1.pooler.supabase.com:6543/postgres"


def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")

    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()