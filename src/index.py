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

import uvicorn, os

from fastapi.responses import RedirectResponse

from src import crear_app

#inicializacion de la aplicación
app = crear_app()

from src.trazabilidad import (
  router as trazabilidad_router,
  prefijo as trazabilidad_prefijo,
  etiquetas as trazabilidad_etiquetas,
)

app.include_router(
  trazabilidad_router,
  prefix=trazabilidad_prefijo,
  tags=trazabilidad_etiquetas,
)

@app.get("/")
async def index():
  return RedirectResponse(url=trazabilidad_prefijo)

from src.encajes import app as encaje

app.mount("/encajes", encaje)

def main():
  from src.config import config

  uvicorn.run(
    "src.index:app",
    host=config["servidor"],
    port=int(config["puerto"]),
    reload=app.debug,
    log_level="debug" if app.debug else "info",
    ws="websockets",
  )

if __name__ == "__main__": main()