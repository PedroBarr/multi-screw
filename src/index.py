#-------------------------------------------------------------------------------
# Nombre:      Indice de Multi Screw
# Proposito:   Servir de indice de direcciones principales para
#               redirigir a las demas funcionalidades de Multi Screw
#               (event-driven).
#
# Autor:       Aref
#
# Creado:      29/9-3/1999+2*(12+1)
# Derechos
# de autor:    (k) Alta Lengua 2025
# Licencia:    <GPLv3>
#-------------------------------------------------------------------------------

""" Modulo: Indice de Multi Screw

Servir de índice de direcciones principales para redirigir a las
demas funcionalidades de Multi Screw (event-driven).

Recopila:
    Aplicativo
"""

import uvicorn
from fastapi import FastAPI

#inicializacion de la aplicación
app = FastAPI(
    title="Multi Screw Event-Driven Backend",
    description="This is the backend for the Multi Screw event-driven application.",
    version="1.0.0",
    contact={
        "name": "Aref",
    },
    license_info={
        "name": "GPLv3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html"
    },
)

@app.get("/")
async def index(): return {"message": "Welcome to Multi Screw Event-Driven Backend"}

def main(): uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__": main()