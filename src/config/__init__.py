#-------------------------------------------------------------------------------
# Nombre:      Configuracion del aplicativo director de eventos
# Proposito:   Empaquetar los ficheros configuradores.
#
# Autor:       Aref
#
# Creado:      29/9-3/1999+2*(12+1)
# Derechos
# de autor:    (k) Alta Lengua 2025
# Licencia:    <GPLv3>
#-------------------------------------------------------------------------------

""" Paquete: Configuracion del aplicativo director de eventos

Empaquetar los ficheros configuradores.


    Modulo: Cabecera del paquete configuracion del aplicativo director de
        eventos

Genera la configuracion del aplicativo director de eventos y la hace llamable.
"""

import json, os

config = {}

ruta = os.path.dirname(os.path.abspath(__file__))

def init_config():
  """ Funcion encapsuladora: Inicializacion de la configuracion

  Funcion que actualiza el diccionario de configuraciones.

  Excepciones:
      RuntimeError (Ningun archivo encontrado para la
          configuracion) -- Si nunca se hallo un archivo valido
  """
  def update_config(cargador: dict):
    """ Funcion encapsulada: Actualizar configuracion

    Funcion que actualiza la configuracion llamable en base a un
    diccionario cargador. Si alguno de los elementos es una
    variable de entorno, llama la variable.

    Parametros:
        cargador (dict) -- diccionario con los valores para
            agregar a la configuracion
    """
    for l, e in cargador.items(): #llaves y elementos del cargador

      #condicional si el elemento a configurar es una variable de entorno
      if type(e) == str and e.startswith('$'): config[l] = os.getenv(e[1:])

      else: config[l] = e

  # Funcion encapsulada: Configurar desde archivo
  def init_config_ruta(ruta_config: str):
    with open(ruta_config) as f: update_config(json.load(f))

  #ruta del JSON
  ruta_final = ruta + f'/config.json'

  try: init_config_ruta(ruta_final)

  except FileNotFoundError:
    print("Ningun archivo para la configuracion")
    raise RuntimeError("Ningun archivo valido encontrado para la " +
      "configuracion")

  config["depurado"] = config.get("entorno") == "development"