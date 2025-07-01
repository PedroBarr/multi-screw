#-------------------------------------------------------------------------------
# Nombre:      Control de recursos del sistema (SRC)
# Proposito:   Empaquetar el aplicativo Multi Screw (event-driven).
#
# Autor:       Aref
#
# Creado:      29/9-3/1999+2*(12+1)
# Derechos
# de autor:    (k) Alta Lengua 2025
# Licencia:    <GPLv3>
#-------------------------------------------------------------------------------

""" Paquete: Control de recursos del sistema (SRC)

Empaquetar el aplicativo Multi Screw (event-driven). Sus dependencias web
y sus aplicativos director de eventos (index) y principal (main).

Las funcionalidades se encuentran en paquetes con planos de
aplicacion. Cada paquete cuenta con al menos una cabecera que
inicializa el plano del paquete, un archivo de rutas (routes) que
registran el acceso a la funcionalidad del plano y usualmente un
modulo de servicios del paquete.


    Modulo: Cabecera del paquete SRC

Este modulo se ejecuta antes que todos los demas e informa a
python que Multi Screw (event-driven) tiene arquitectura de paquete.

Recopila:
    Funcion Fabrica de aplicativo
    Paquetes Configuracion del aplicativo
"""

import os

from fastapi import FastAPI

from src.config import config, init_config

def crear_app() -> FastAPI:
  """ Funcion: Fabrica de aplicativo

  Funcion que genera una aplicacion web y la configura
  implementando el patron fabrica de aplicativo.

  Retorno:
      un aplicativo de red configurado
  """
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

  init_config()

  app.debug = config.get("depurado", False)

  return app