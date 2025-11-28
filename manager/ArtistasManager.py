# Clase gestora para operaciones de base de datos relacionadas con Artistas
import sqlite3
from models.models import Artista
from manager.conexionManager import get_cursor

class ArtistaManager:
    """
    Gestiona todas las operaciones de base de datos relacionadas con artistas
    """
    
    def addArtista(self, artista: Artista) -> str:
        """
        Agrega un nuevo artista a la base de datos
        Args:
            artista: Objeto Artista que contiene el nombre
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            str: Mensaje de confirmación
        """
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO artistas (nombre) VALUES (?)",
                (artista.nombre,),
            )
            return "Artista creado exitosamente"

    def getArtistas(self) -> list:
        """
        Obtiene todos los artistas de la base de datos
        Args:
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista de diccionarios que contienen información de artistas
        """
        with get_cursor() as cursor:
            res = cursor.execute("SELECT * FROM artistas").fetchall()
            return [{"id": row[0], "nombre": row[1]} for row in res]

    def getArtistaForId(self, id: int) -> list:
        """
        Obtiene un artista por su ID
        Args:
            id: ID del artista a buscar
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista que contiene la información del artista encontrado
        """
        with get_cursor() as cursor:
            res = cursor.execute(
                "SELECT id_artista,nombre FROM artistas WHERE id_artista = ?", (id,)
            ).fetchall()
            return [{"id": row[0], "nombre": row[1]} for row in res]

    def modificarArtista(
        self, id: int, modificarArtista: Artista
    ) -> str:
        """
        Update an artist's information
        Args:
            id: ID of the artist to update
            modificarArtista: Artist object with new information
            cursor: Database cursor for executing queries
        Returns:
            str: Confirmation message
        """
        with get_cursor() as cursor:
            cursor.execute(
                "UPDATE artistas SET nombre = ? WHERE id_artista = ?",
                (modificarArtista.nombre, id),
            )
            return "Artista modificado exitosamente"

    def deleteClient(self, id: int) -> str:
        """
        Delete an artist from the database
        Args:
            id: ID of the artist to delete
            cursor: Database cursor for executing queries
        Returns:
            str: Confirmation message
        """
        with get_cursor() as cursor:
            cursor.execute("DELETE FROM artistas WHERE id_artista = ?", (id,))
            return "Artista eliminado exitosamente"