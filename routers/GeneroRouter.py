import psycopg
from fastapi import APIRouter, Depends
from manager.conexionManagerSupabase import getCursor
from manager.GeneroManager import GeneroManager
from models.models import Genero

generoManager = GeneroManager()
router = APIRouter(prefix="/generos", tags=["Generos router"])


@router.get("/obtener_generos")
def getProductos(cursor: psycopg.Cursor = Depends(getCursor)):
    res = generoManager.getGenero(cursor)
    return res


@router.post("/crear_genero")
def postGenero(genero: Genero, cursor: psycopg.Cursor = Depends(getCursor)):
    res = generoManager.addGenero(genero, cursor)
    return {"msg": res}