from fastapi import APIRouter
from manager.MusicaManager import MusicaManager
from models.models import Musica

router = APIRouter(prefix="/musica", tags=["Música"])
musicaManager = MusicaManager()

@router.get("/")
def getMusica():
    return musicaManager.getMusica()

@router.get("/{id}")
def getMusicaForId(id: int):
    return musicaManager.getMusicaForId(id)

@router.get("/artista/{nombre}")
def getMusicaForArtista(nombre: str):
    return musicaManager.getMusicaForArtista(nombre)

@router.post("/")
def postMusica(musica: Musica):
    res = musicaManager.addMusica(musica)
    return {"mensaje": res}

@router.delete("/{id}")
def deleteMusica(id: int):
    res = musicaManager.deleteMusica(id)
    return {"mensaje": res}