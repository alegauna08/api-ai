import psycopg
from fastapi import APIRouter, Depends
from manager.CancionManager import CancionManager
from manager.conexionManagerSupabase import getCursor
from models.models import Cancion

# Creación de router
router = APIRouter(prefix="/canciones", tags=["Canciones routes"])
CancionManager = CancionManager()
@router.get("/obtener_canciones")
def getCanciones(cursor: psycopg.Cursor = Depends(getCursor)):
    res = CancionManager.getCanciones(cursor)
    return res
@router.get("/obtener_cancion/{id}")
def getCancionForId(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = CancionManager.getCancionForId(id, cursor)
    return res
@router.post("/crear_Cancion")
def postCancion(cancion: Cancion, cursor: psycopg.Cursor = Depends(getCursor)):
    res = CancionManager.addCancion(cancion, cursor)
    return {"msg": res}
@router.put("/modificar_Cancion/{id}")
def putCancion(
    id: int, CancionUpdated: Cancion, cursor: psycopg.Cursor = Depends(getCursor)
):
    res = CancionManager.modificarCancion(id, CancionUpdated, cursor)
    return {"msg", res}
@router.delete("/eliminar_Cancion/{id}")
def deleteCancion(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = CancionManager.deleteCancion(id, cursor)
    return {"msg": res}