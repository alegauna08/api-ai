import psycopg
from fastapi import APIRouter, Depends
from manager.ArtistasManager import ArtistaManager
from manager.conexionManagerSupabase import getCursor
from models.models import Artista

# Creación de router
router = APIRouter(prefix="/artistas", tags=["Artistas routes"])
ArtistaManager = ArtistaManager()


@router.get("/obtener_artistas")
def getArtistas(cursor: psycopg.Cursor = Depends(getCursor)):
    res = ArtistaManager.getArtistas(cursor)
    return res


@router.get("/obtener_artista/{id}")
def getArtistaForId(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = ArtistaManager.getArtistaForId(id, cursor)
    return res


@router.post("/crear_Artista")
def postArtista(artista: Artista, cursor: psycopg.Cursor = Depends(getCursor)):
    res = ArtistaManager.addArtista(Artista, cursor)
    return {"msg": res}


@router.put("/modificar_Artista/{id}")
def putArtista(
    id: int, ArtistaUpdated: Artista, cursor: psycopg.Cursor = Depends(getCursor)
):
    res = ArtistaManager.modificarArtista(id, ArtistaUpdated, cursor)
    return {"msg", res}


@router.delete("/eliminar_Artista/{id}")
def deleteArtista(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = ArtistaManager.deleteArtista(id, cursor)
    return {"msg": res}