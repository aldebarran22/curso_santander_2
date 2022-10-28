"""
Implementación del servidor TCP
"""

import socket as s
import sys

if len(sys.argv)==2:
    puerto = int(sys.argv[1])
else:
    raise ValueError("Se requiere un número de puerto > 1024")

sock = None
sc = None
try:
    sock = s.socket()
    #s.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR,1)
    sock.bind(("localhost", puerto))
    sock.listen(1)
    print('Socket creado a la espera de clientes!')
    sc, addr = sock.accept()
    while True:
        recibido =  sc.recv(1024)
        recibido = recibido.decode('utf-8')
        if recibido == "quit": break
        print("Recibido:", recibido)
        sc.send(recibido.encode('utf-8'))

    print("fin")
except Exception as e:
    print(e)

finally:
    if sc: sc.close()
    if sock: sock.close()

