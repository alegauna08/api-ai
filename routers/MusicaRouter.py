import psycopg
from fastapi import APIRouter, Depends
from manager.conexionManagerSupabase import getCursor
from manager.MusicaManager import MusicaManager
from models.models import Musica

MusicaManager = MusicaManager()
router = APIRouter(prefix="/musica", tags=["Musica router"])


@router.post("/crear_Musica")
def postMusica(musica: Musica, cursor: psycopg.Cursor = Depends(getCursor)):
    res = MusicaManager.addMusica(musica, cursor)
    return {"msg": res}


@router.get("/obtener_musicas")
def getMusica(cursor: psycopg.Cursor = Depends(getCursor)):
    res = MusicaManager.getMusica(cursor)
    return res


@router.get("/obtener_musica/{id}")
def getMusicaForId(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = MusicaManager.getMusicaForId(id, cursor)
    return res


@router.get("/obtener_musica_por_artita/{nombre}")
def getMusicaForArtista(nombre: str, cursor: psycopg.Cursor = Depends(getCursor)):
    res = MusicaManager.getMusicaForArtista(nombre, cursor)
    return res