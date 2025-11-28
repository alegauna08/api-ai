# Clase gestora para operaciones de base de datos relacionadas con Canciones
import sqlite3
from models.models import Cancion
from manager.conexionManager import get_cursor

class CancionManager:
    """
    Gestiona todas las operaciones de base de datos relacionadas con canciones
    """
    
    def addCancion(self, cancion: Cancion) -> str:
        """
        Add a new song to the database
        Args:
            cancion: Song object containing the name and artist
            cursor: Database cursor for executing queries
        Returns:
            str: Confirmation message
        """
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO cancion (nombre, id_artista) VALUES (?, ?)",
                (cancion.nombre, cancion.artistaNombre),
            )
            return "Canción creada exitosamente"

    def getCanciones(self) -> list:
        """
        Obtiene todas las canciones de la base de datos
        Args:
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista de diccionarios que contienen información de canciones
        """
        with get_cursor() as cursor:
            res = cursor.execute("SELECT * FROM cancion").fetchall()
            return [{"id": row[0], "nombre": row[1], "id_artista": row[2]} for row in res]

    def getCancionForId(self, id: int) -> list:
        """
        Retrieve a song by its ID
        Args:
            id: Song ID to search for
            cursor: Database cursor for executing queries
        Returns:
            list: List containing the matching song's information
        """
        with get_cursor() as cursor:
            res = cursor.execute(
                "SELECT id_cancion, nombre, id_artista FROM cancion WHERE id_cancion = ?", (id,)
            ).fetchall()
            return [{"id": row[0], "nombre": row[1], "id_artista": row[2]} for row in res]

    def modificarCancion(
        self, id: int, modificarCancion: Cancion
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
        with get_cursor() as cursor:
            cursor.execute(
                "UPDATE cancion SET nombre = ?, id_artista = ? WHERE id_cancion = ?",
                (modificarCancion.nombre, modificarCancion.artistaNombre, id),
            )
            return "Canción modificada exitosamente"

    def deleteCancion(self, id: int) -> str:
        """
        Delete a song from the database
        Args:
            id: ID of the song to delete
            cursor: Database cursor for executing queries
        Returns:
            str: Confirmation message
        """
        with get_cursor() as cursor:
            cursor.execute("DELETE FROM cancion WHERE id_cancion = ?", (id,))
            return "Canción eliminada exitosamente"