#-------------------------------------------------------------------------------
# Nombre:      Control de recursos de la trazabilidad
# Proposito:   Empaquetar los recursos de la trazabilidad.
#
# Autor:       Aref
#
# Creado:      3-1/7/1999+2*(12+1)
# Derechos
# de autor:    (k) Alta Lengua 2025
# Licencia:    <GPLv3>
#-------------------------------------------------------------------------------

trazabilidad = {
  "title": "Aplicativo dorsal director de eventos Multi Screw",
  "description": "Este aplicativo sirve como director de eventos para el sistema Multi Screw, gestionando las funcionalidades de encajes.",
  "version": "1.0.1",
  "contact": {
      "name": "Aref",
  },
  "license_info": {
      "name": "GPLv3",
      "url": "https://www.gnu.org/licenses/gpl-3.0.html"
  },
}

prefijo = "/acerca_de"

etiquetas = ["acerca_de"]

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def acerca_de():
  return {
    "nombre": trazabilidad["title"],
    "descripcion": trazabilidad["description"],
    "version": trazabilidad["version"],
    "autor": trazabilidad["contact"]["name"],
    "licencia": trazabilidad["license_info"]["name"],
  }