# Models definition file
# This file contains all the Pydantic models used for data validation in the API

from pydantic import BaseModel


class Musica(BaseModel):
    """
    Model for relating songs with artists and genres
    """
    id_cancion: int    # ID of the song
    id_cantante: int   # ID of the artist
    id_genero: int     # ID of the genre


class Artista(BaseModel):
    """
    Model for artist information
    """
    nombre: str        # Name of the artist


class Cancion(BaseModel):
    """
    Model for song information
    """
    nombre: str        # Name of the song
    artistaNombre: str # Name or ID of the artist who performs the song

class Genero(BaseModel):
    """
    Model for music genres
    """
    nombre: str        # Name of the genre