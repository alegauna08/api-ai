from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.ArtistasRouter import router as router_artistas
from routers.MusicaRouter import router as router_musica
from routers.GeneroRouter import router as router_generos
from routers.CancionRouter import router as router_canciones
from manager.conexionManagerSupabase import init_db

# Crear instancia de FastAPI
app = FastAPI(
    title="API de Música",
    description="API para gestionar música, artistas, canciones y géneros",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Evento de inicio
@app.on_event("startup")
async def startup_event():
    init_db()

# Incluir todos los routers
app.include_router(router_artistas, prefix="/api/v1")
app.include_router(router_generos, prefix="/api/v1")
app.include_router(router_musica, prefix="/api/v1")
app.include_router(router_canciones, prefix="/api/v1")

# Ruta raíz
@app.get("/")
async def root():
    return {
        "mensaje": "Bienvenido a la API de Música",
        "documentacion": "/docs",
        "version": "1.0.0"
    }