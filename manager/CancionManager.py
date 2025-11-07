# Manager class for handling Song-related database operations
import psycopg
from models.models import Cancion

class CancionManager:
    """
    Manages all database operations related to songs
    """
    
    def addCancion(self, cancion: Cancion, cursor: psycopg.Cursor):
        """
        Add a new song to the database
        Args:
            cancion: Song object containing the name and artist
            cursor: Database cursor for executing queries
        Returns:
            str: Confirmation message
        """
        cursor.execute(
            "INSERT INTO canciones (nombre) VALUES (%s,)",
            (cancion.nombre, cancion.artistaNombre),
        )
        return f"cancion creada"

    def getCanciones(self, cursor: psycopg.Cursor) -> list:
        """
        Obtiene todas las canciones de la base de datos
        Args:
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista de diccionarios que contienen información de canciones
        """
        res = cursor.execute("SELECT * FROM canciones").fetchall()
        return [{"id": row[0], "nombre": row[1], "id_artista": row[2]} for row in res]

    def getCancionForId(self, id: int, cursor: psycopg.Cursor) -> list:
        """
        Retrieve a song by its ID
        Args:
            id: Song ID to search for
            cursor: Database cursor for executing queries
        Returns:
            list: List containing the matching song's information
        """
        res = cursor.execute(
            "SELECT id_cancion,nombre FROM canciones WHERE id_cancion = %s", (id,)
        ).fetchall()
        return [{"id": row[0], "nombre": row[1], "id_artista": row[2],} for row in res]

    def modificarCancion(
        self, id: int, modificarCancion: Cancion, cursor: psycopg.Cursor
    ) -> str:
        """
        Update a song's information
        Args:
            id: ID of the song to update
            modificarCancion: Song object with new information
            cursor: Database cursor for executing queries
        Returns:
            str: Confirmation message
        """
        cursor.execute(
            "UPDATE canciones SET nombre = %s WHERE id_cancion = %s",
            ( modificarCancion.nombre, id),
        )
        return "Cancion modificada!"

    def deleteCancion(self, id: int, cursor: psycopg.Cursor) -> str:
        """
        Delete a song from the database
        Args:
            id: ID of the song to delete
            cursor: Database cursor for executing queries
        Returns:
            str: Confirmation message
        """
        cursor.execute("DELETE FROM canciones WHERE id_cancion = %s", (id,))
        return "Cancion eliminada"