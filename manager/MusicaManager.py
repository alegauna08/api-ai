# Clase gestora para operaciones de base de datos relacionadas con Música
import psycopg
from models.models import Musica

class MusicaManager:
    """
    Gestiona todas las operaciones de base de datos relacionadas con entradas musicales
    Esta clase maneja las relaciones entre canciones, artistas y géneros
    """
    
    def getMusica(self, cursor: psycopg.Cursor) -> list:
        """
        Obtiene todas las entradas musicales con su información relacionada
        Args:
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista de diccionarios que contienen información musical combinada
        """
        res = cursor.execute(
            "SELECT genero.nombre, artista.nombre, cancion.nombre FROM musica INNER JOINq artista ON musica.id_artista = artista.id_artista INNER JOIN genero ON musica.id_genero = genero.id_genero INNER JOIN cancion ON musica.id_cancion = cancion.id_cancion"
        ).fetchall()
        return [
            {"genero": row[0], "artista": row[1], "cancion": row[2]} for row in res
        ]

    def getMusicaForId(self, id: int, cursor: psycopg.Cursor) -> list:
        """
        Obtiene una entrada musical por su ID con toda la información relacionada
        Args:
            id: ID de la entrada musical a buscar
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista que contiene la información de la entrada musical encontrada
        """
        res = cursor.execute(
            "SELECT genero.nombre, artista.nombre, cancion.nombre FROM musica INNER JOIN artista ON musica.id_artista = artista.id_artista INNER JOIN genero ON musica.id_genero = genero.id_genero INNER JOIN cancion ON musica.id_cancion WHERE musica.id_cancion = %s",
            (id,),
        ).fetchall()
        return [
            {"genero": row[0], "artista": row[1], "cancion": row[2]} for row in res
        ]

    def getMusicaForArtista(self, nombre: str, cursor: psycopg.Cursor) -> list | str:
        """
        Obtiene todas las entradas musicales para un artista específico
        Args:
            nombre: Nombre del artista a buscar
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            list: Lista de diccionarios que contienen información musical del artista
            str: Mensaje de error si no se encuentra el artista
        """
        idArtista = cursor.execute(
            "SELECT id_artista FROM artista WHERE nombre = (%s)", (nombre,)
        ).fetchone()
        if idArtista:
            res = cursor.execute(
                "SELECT cancion.nombre, genero.nombre, artusta.nombre FROM musica INNER JOIN cancion ON musica.id_cancion = cancion.id_cancion INNER JOIN genero ON musica.id_genero = genero.id_genero INNER JOIN artista ON musica.id_artista WHERE musica.id_artista = %s",
                (idArtista[0],),
            ).fetchall()
            return [
                {"cancion": row[0], "genero": row[1], "artista": row[2]} for row in res
            ]
        else:
            return "Error, atistas no encontrado"

    def addMusica(self, musica: Musica, cursor: psycopg.Cursor):
        """
        Agrega una nueva entrada musical vinculando una canción con su artista y género
        Args:
            musica: Objeto Musica que contiene los IDs de relación
            cursor: Cursor de base de datos para ejecutar consultas
        Returns:
            str: Mensaje de confirmación
        """
        cursor.execute(
            "INSERT INTO musica (id_genero, id_artista, id_cancio) VALUES (%s,%s,%s)",
            (musica.id_genero, musica.id_artista, musica.id_cancion),
        )
        return "musica agregada exitosamente"