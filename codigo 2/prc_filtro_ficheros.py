"""
Filtrar los ficheros de una carpeta que tengan una determinada extensión (varias)
"""

import os

L = os.listdir()
t = ('py','txt')
for f in L:
    if f.partition('.')[2] in t:
        print(f)