# Clase gestora para operaciones de base de datos relacionadas con Géneros
import sqlite3
from models.models import Genero
from manager.conexionManager import get_cursor

class GeneroManager:
    """
    Gestiona todas las operaciones de base de datos relacionadas con géneros musicales
    """
    
    def addGenero(self, genero: Genero) -> str:
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO genero (nombre) VALUES (?)",
                (genero.nombre,)
            )
            return "Género agregado exitosamente"

    def getGeneros(self) -> list:
        with get_cursor() as cursor:
            res = cursor.execute("SELECT * FROM genero").fetchall()
            return [
                {"id": row[0], "nombre": row[1]} for row in res
            ]
            
    def getGeneroById(self, id: int) -> list:
        """
        Obtiene un género por su ID
        """
        with get_cursor() as cursor:
            res = cursor.execute(
                "SELECT id_genero, nombre FROM genero WHERE id_genero = ?", (id,)
            ).fetchall()
            return [{"id": row[0], "nombre": row[1]} for row in res]
            
    def deleteGenero(self, id: int) -> str:
        """
        Elimina un género por su ID
        """
        with get_cursor() as cursor:
            cursor.execute("DELETE FROM genero WHERE id_genero = ?", (id,))
            return "Género eliminado exitosamente"