# Clase gestora para operaciones de base de datos relacionadas con Música
import sqlite3
from models.models import Musica
from manager.conexionManager import get_cursor

class MusicaManager:
    """
    Gestiona todas las operaciones de base de datos relacionadas con entradas musicales
    Esta clase maneja las relaciones entre canciones, artistas y géneros
    """
    
    def getMusica(self) -> list:
        """
        Obtiene todas las entradas musicales con su información relacionada
        Args:
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista de diccionarios que contienen información musical combinada
        """
        with get_cursor() as cursor:
            res = cursor.execute("""
                SELECT genero.nombre, artistas.nombre, cancion.nombre 
                FROM musica 
                INNER JOIN artistas ON musica.id_artista = artistas.id_artista 
                INNER JOIN genero ON musica.id_genero = genero.id_genero 
                INNER JOIN cancion ON musica.id_cancion = cancion.id_cancion
            """).fetchall()
            return [
                {"genero": row[0], "artista": row[1], "cancion": row[2]} for row in res
            ]

    def getMusicaForId(self, id: int) -> list:
        """
        Obtiene una entrada musical por su ID con toda la información relacionada
        Args:
            id: ID de la entrada musical a buscar
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista que contiene la información de la entrada musical encontrada
        """
        with get_cursor() as cursor:
            res = cursor.execute("""
                SELECT genero.nombre, artistas.nombre, cancion.nombre 
                FROM musica 
                INNER JOIN artistas ON musica.id_artista = artistas.id_artista 
                INNER JOIN genero ON musica.id_genero = genero.id_genero 
                INNER JOIN cancion ON musica.id_cancion = cancion.id_cancion 
                WHERE musica.id_musica = ?
            """, (id,)).fetchall()
            return [
                {"genero": row[0], "artista": row[1], "cancion": row[2]} for row in res
            ]

    def getMusicaForArtista(self, nombre: str) -> list | str:
        """
        Obtiene todas las entradas musicales para un artista específico
        Args:
            nombre: Nombre del artista a buscar
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista de diccionarios que contienen información musical del artista
            str: Mensaje de error si no se encuentra el artista
        """
        with get_cursor() as cursor:
            idArtista = cursor.execute(
                "SELECT id_artista FROM artistas WHERE nombre = ?", (nombre,)
            ).fetchone()
            if idArtista:
                res = cursor.execute("""
                    SELECT cancion.nombre, genero.nombre, artistas.nombre 
                    FROM musica 
                    INNER JOIN cancion ON musica.id_cancion = cancion.id_cancion 
                    INNER JOIN genero ON musica.id_genero = genero.id_genero 
                    INNER JOIN artistas ON musica.id_artista = artistas.id_artista 
                    WHERE musica.id_artista = ?
                """, (idArtista[0],)).fetchall()
                return [
                    {"cancion": row[0], "genero": row[1], "artista": row[2]} for row in res
                ]
            else:
                return "Error: Artista no encontrado"

    def addMusica(self, musica: Musica) -> str:
        """
        Agrega una nueva entrada musical vinculando una canción con su artista y género
        Args:
            musica: Objeto Musica que contiene los IDs de relación
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            str: Mensaje de confirmación
        """
        with get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO musica (id_genero, id_artista, id_cancion) VALUES (?, ?, ?)",
                (musica.id_genero, musica.id_cantante, musica.id_cancion),
            )
            return "Música agregada exitosamente"
            
    def deleteMusica(self, id: int) -> str:
        """
        Elimina una entrada musical por su ID
        """
        with get_cursor() as cursor:
            cursor.execute("DELETE FROM musica WHERE id_musica = ?", (id,))
            return "Entrada musical eliminada exitosamente"