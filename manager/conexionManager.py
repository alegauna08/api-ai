import sqlite3
from typing import Generator

def getCursor() -> Generator[sqlite3.Cursor, None, None]:
    conn = sqlite3.connect("musica.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def initeDB() -> None:
        connection = sqlite3.connect("musica.db", check_same_thread=False)
        try:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS artistas (id_artista INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)"
            )
            connection.execute(
                "CREATE TABLE IF NOT EXISTS genero (id_genero INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)"
            )
            connection.execute(
                "CREATE TABLE IF NOT EXISTS cancion (id_cancion INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)"
            )
            connection.execute(
                "CREATE TABLE IF NOT EXISTS musica (id_cancion INTEGER PRIMARY KEY AUTOINCREMENT, id_genero INTEGER, id_artista INTEGER, id_cancion FOREIGN KEY (id_artista) REFERENCES artistas(id_artista), FOREIGN KEY (id_genero) REFERENCES genero(id_genero), FOREIGN KEY (id_cancion) REFERENCES cancion(id_cancio) )"
            )
            connection.commit()
        finally:
            connection.close()
            print("DB Inicializada")