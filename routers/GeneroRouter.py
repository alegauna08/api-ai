from fastapi import APIRouter
from manager.GeneroManager import GeneroManager
from models.models import Genero

router = APIRouter(prefix="/generos", tags=["Géneros"])
generoManager = GeneroManager()

@router.get("/")
def getGeneros():
    return generoManager.getGeneros()

@router.get("/{id}")
def getGeneroById(id: int):
    return generoManager.getGeneroById(id)

@router.post("/")
def postGenero(genero: Genero):
    res = generoManager.addGenero(genero)
    return {"mensaje": res}

@router.delete("/{id}")
def deleteGenero(id: int):
    res = generoManager.deleteGenero(id)
    return {"mensaje": res}