#-------------------------------------------------------------------------------
# Nombre:      Control de recursos del sistema de encajes
# Proposito:   Empaquetar el aplicativo de encajes (sockets).
#
# Autor:       Aref
#
# Creado:      1/7/1999+2*(12+1)
# Derechos
# de autor:    (k) Alta Lengua 2025
# Licencia:    <GPLv3>
#-------------------------------------------------------------------------------

import socketio

encaje = socketio.AsyncServer(
  async_mode='asgi',
  cors_allowed_origins='*',
)

app = socketio.ASGIApp(
  encaje,
  socketio_path="/encajes/socket.io",
)

@encaje.on('connect')
async def connect(id_sesion, env_vars):
    print(f'Client {id_sesion} connected')
    await encaje.emit('message', 'Welcome to the encaje server!', room=id_sesion)

@encaje.on('disconnect')
async def disconnect(id_sesion):
    print(f'Client {id_sesion} disconnected')
    await encaje.emit('message', 'Goodbye!', room=id_sesion)