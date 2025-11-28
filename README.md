<<<<<<< HEAD
# api-router-test
=======
# Proyecto FastAPI - Canciones y Descompresión

Este repositorio contiene una pequeña API construida con FastAPI para gestionar canciones, junto con utilidades para descomprimir archivos (.zip y .rar).

Estructura principal:

- `main.py` - Punto de entrada de la aplicación FastAPI.
- `routers/` - Routers para clientes, pedidos y productos.
- `manager/` - Lógica de acceso a datos y managers de la aplicación.
- `models/` - Modelos Pydantic y/o definiciones de datos.
- `descomprimir.py` - Utilidad para descomprimir archivos (zip/rar).

Cómo ejecutar localmente (Windows, PowerShell):

1. Activar el entorno virtual:

```powershell
.\env\Scripts\Activate.ps1
```

2. Instalar dependencias (si faltan):

```powershell
pip install -r requirements.txt
# o instalar manualmente: pip install fastapi uvicorn rarfile psycopg
```

3. Ejecutar la aplicación:

```powershell
uvicorn main:app --reload
```

Subir a GitHub:

- Si ya tienes un repo remoto: configura `git remote add origin <url>` y `git push -u origin main`.
- Si no lo tienes, puedes crear uno en GitHub y usar `gh repo create` o crear el remoto desde la web.

Notas:
- Si quieres que traiga el `README.md` y el `.gitignore` desde un repositorio de GitHub específico, pásame la URL del repo (o el usuario/repo y la rama). Te doy los comandos exactos para descargar los ficheros crudos y reemplazarlos en tu workspace.
>>>>>>> b907653 (Initial commit: add project files)
