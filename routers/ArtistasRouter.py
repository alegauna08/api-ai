from fastapi import APIRouter
from manager.ArtistasManager import ArtistaManager
from models.models import Artista

# Creación de router
router = APIRouter(prefix="/artistas", tags=["Artistas routes"])
artistaManager = ArtistaManager()

@router.get("/obtener_artistas")
def getArtistas():
    return artistaManager.getArtistas()


@router.get("/obtener_artista/{id}")
def getArtistaForId(id: int):
    return artistaManager.getArtistaForId(id)

@router.post("/crear_artista")
def postArtista(artista: Artista):
    res = artistaManager.addArtista(artista)
    return {"mensaje": res}

@router.put("/modificar_artista/{id}")
def putArtista(id: int, artistaActualizado: Artista):
    res = artistaManager.modificarArtista(id, artistaActualizado)
    return {"mensaje": res}

@router.delete("/eliminar_artista/{id}")
def deleteArtista(id: int):
    res = artistaManager.deleteClient(id)
    return {"mensaje": res}