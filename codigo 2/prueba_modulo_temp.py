"""
Prueba a importar un modulo que se encuentra en la carpeta: D:/temp
modulo_temp.py  funcion()
"""

import sys

sys.path.append("D:/temp")

from modulo_temp import funcion

funcion(123)