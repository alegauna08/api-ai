import os
from typing import Generator
from contextlib import contextmanager

import psycopg
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener credenciales de Supabase
SUPABASE_DB = os.getenv("SUPABASE_DB", "postgres")
SUPABASE_HOST = os.getenv("SUPABASE_HOST")
SUPABASE_PASSWORD = os.getenv("SUPABASE_PASSWORD")
SUPABASE_PORT = os.getenv("SUPABASE_PORT", "6543")
SUPABASE_USER = os.getenv("SUPABASE_USER", "postgres")

# Construir URL de conexión
DATABASE_URL = f"postgresql://{SUPABASE_USER}:{SUPABASE_PASSWORD}@{SUPABASE_HOST}:{SUPABASE_PORT}/{SUPABASE_DB}"

def init_db() -> None:
    """
    Inicializa la conexión a la base de datos y verifica que esté funcionando.
    """
    try:
        with psycopg.connect(DATABASE_URL, sslmode="require") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()
                print(f"Conexión exitosa a Supabase PostgreSQL: {version[0]}")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise

@contextmanager
def getCursor() -> Generator[psycopg.Cursor, None, None]:
    """
    Proporciona un cursor de base de datos en un contexto manejado.
    Garantiza que la conexión y el cursor se cierren correctamente.
    """
    conn = psycopg.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()