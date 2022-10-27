import socket as s

import sys

if len(sys.argv)==2:
    puerto = int(sys.argv[1])
else:
    raise ValueError("Se requiere un número de puerto > 1024")

sock = s.socket ()
sock.connect(("localhost", puerto))
while True:
    mensaje = input(">")
    sock.send(mensaje.encode('utf-8'))
    recibido = sock.recv(1024)
    recibido = recibido.decode('utf-8')
    if mensaje == "quit": break

print('fin cliente')
sock.close()
