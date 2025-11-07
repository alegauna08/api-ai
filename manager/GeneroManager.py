import psycopg
from models.models import Genero


class GeneroManager:
    def addProducto(self, genero: Genero, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO genero (nombre) VALUES (%s,)",
            (genero.nombre),
        )
        return "Genero agregado"

    def getGenero(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT * FROM genero ").fetchall()
        return [
            {"id_generoo": row[0], "nombre": row[1]} for row in res
        ]