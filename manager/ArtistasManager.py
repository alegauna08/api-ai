# Clase gestora para operaciones de base de datos relacionadas con Artistas
import psycopg
from models.models import Artista

class ArtistaManager:
    """
    Gestiona todas las operaciones de base de datos relacionadas con artistas
    """
    
    def addArtista(self, artista: Artista, cursor: psycopg.Cursor):
        """
        Agrega un nuevo artista a la base de datos
        Args:
            artista: Objeto Artista que contiene el nombre
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            str: Mensaje de confirmación
        """
        cursor.execute(
            "INSERT INTO artistas (nombre) VALUES (%s)",
            (artista.nombre,),
        )
        return f"artista creado"

    def getArtistas(self, cursor: psycopg.Cursor) -> list:
        """
        Obtiene todos los artistas de la base de datos
        Args:
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista de diccionarios que contienen información de artistas
        """
        res = cursor.execute("SELECT * FROM artistas").fetchall()
        return [{"id": row[0], "nombre": row[1]} for row in res]

    def getArtistaForId(self, id: int, cursor: psycopg.Cursor) -> list:
        """
        Obtiene un artista por su ID
        Args:
            id: ID del artista a buscar
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista que contiene la información del artista encontrado
        """
        res = cursor.execute(
            "SELECT id_artista,nombre FROM artistas WHERE id_artista = %s", (id,)
        ).fetchall()
        return [{"id": row[0], "nombre": row[1]} for row in res]

    def modificarArtista(
        self, id: int, modificarArtista: Artista, cursor: psycopg.Cursor
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
        cursor.execute(
            "UPDATE artistas SET nombre = %s WHERE id_cliente = %s",
            ( modificarArtista.nombre, id),
        )
        return "Artista modificado!"

    def deleteClient(self, id: int, cursor: psycopg.Cursor) -> str:
        """
        Delete an artist from the database
        Args:
            id: ID of the artist to delete
            cursor: Database cursor for executing queries
        Returns:
            str: Confirmation message
        """
        cursor.execute("DELETE FROM artistas WHERE id_artista = %s", (id,))
        return "Artista eliminado"