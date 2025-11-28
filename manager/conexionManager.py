import sqlite3
from contextlib import contextmanager
from typing import Generator
import os
from pathlib import Path

# Determinar si estamos en Vercel o en desarrollo local
IS_VERCEL = os.environ.get('VERCEL_ENV') is not None

# En Vercel, usar /tmp para almacenar la base de datos
if IS_VERCEL:
    DATABASE_PATH = "/tmp/musica.db"
else:
    # En desarrollo local, usar el directorio del proyecto
    DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "musica.db")

@contextmanager
def get_connection():
    # Asegurarse de que el directorio existe
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    connection = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()

@contextmanager
def get_cursor():
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            yield cursor
            connection.commit()
        finally:
            cursor.close()

def initeDB() -> None:
    with get_connection() as connection:
        try:
            # Crear tablas si no existen
            connection.execute("""
                CREATE TABLE IF NOT EXISTS artistas (
                    id_artista INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE
                )
            """)
            
            connection.execute("""
                CREATE TABLE IF NOT EXISTS genero (
                    id_genero INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE
                )
            """)
            
            connection.execute("""
                CREATE TABLE IF NOT EXISTS cancion (
                    id_cancion INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    id_artista INTEGER,
                    FOREIGN KEY (id_artista) REFERENCES artistas(id_artista)
                )
            """)
            
            connection.execute("""
                CREATE TABLE IF NOT EXISTS musica (
                    id_musica INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_genero INTEGER,
                    id_artista INTEGER,
                    id_cancion INTEGER,
                    FOREIGN KEY (id_artista) REFERENCES artistas(id_artista),
                    FOREIGN KEY (id_genero) REFERENCES genero(id_genero),
                    FOREIGN KEY (id_cancion) REFERENCES cancion(id_cancion)
                )
            """)
            
            # Insertar algunos datos de ejemplo si las tablas están vacías
            if not connection.execute("SELECT * FROM genero").fetchall():
                connection.execute("INSERT INTO genero (nombre) VALUES (?)", ("Rock",))
                connection.execute("INSERT INTO genero (nombre) VALUES (?)", ("Pop",))
                connection.execute("INSERT INTO genero (nombre) VALUES (?)", ("Jazz",))

            connection.commit()
            print("Base de datos inicializada correctamente")
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
            raise