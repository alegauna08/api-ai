# Main application file for the Music API
# This file initializes the FastAPI application and includes all the routers

from fastapi import FastAPI
from routers.ArtistasRouter import router as routerClientes       # Router for artist-related endpoints
from routers.MusicaRouter import router as routerPedidos         # Router for music-related endpoints
from routers.GeneroRouter import router as routerProductos       # Router for genre-related endpoints
from routers.CancionRouter import router as routerCanciones      # Router for song-related endpoints

# Create FastAPI application instance
app = FastAPI()

# Include all routers in the application
app.include_router(routerClientes)      # Add endpoints for artists
app.include_router(routerProductos)     # Add endpoints for genres
app.include_router(routerPedidos)       # Add endpoints for music
app.include_router(routerCanciones)     # Add endpoints for songs