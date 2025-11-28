from fastapi import APIRouter
from manager.CancionManager import CancionManager
from models.models import Cancion

# Creación de router
router = APIRouter(prefix="/canciones", tags=["Canciones"])
cancionManager = CancionManager()

@router.get("/")
def getCanciones():
    return cancionManager.getCanciones()
@router.get("/{id}")
def getCancionForId(id: int):
    return cancionManager.getCancionForId(id)

@router.post("/")
def postCancion(cancion: Cancion):
    res = cancionManager.addCancion(cancion)
    return {"mensaje": res}

@router.put("/{id}")
def putCancion(id: int, cancionActualizada: Cancion):
    res = cancionManager.modificarCancion(id, cancionActualizada)
    return {"mensaje": res}

@router.delete("/{id}")
def deleteCancion(id: int):
    res = cancionManager.deleteCancion(id)
    return {"mensaje": res}