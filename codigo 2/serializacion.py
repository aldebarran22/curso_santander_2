"""
Ejemplo de serializacion en Python
Serializar un diccinario con listas de objetos
"""

from poo2 import Punto2D
from random import randint
import pickle as p
import string, shelve

def serializar(path, obj):
    f = None
    try:
        f = open(path, "wb")
        p.dump(obj, f, protocol=2)

    except Exception as e:
        print(e)

    finally:
        if f:f.close()

def deserializar(path):
    f = None
    try:
        f = open(path, "rb")
        d = p.load(f)
        return d

    except Exception as e:
        print(e)
        
    finally:
        if f:f.close()

def serializar2(path, obj, L):
    Shelf = None
    try:
        Shelf = shelve.open(path,protocol=2)
        Shelf['obj'] = obj
        Shelf['L'] = L

    except Exception as e:
        print("ERROR al serializar",e)

    finally:
        if Shelf: Shelf.close

def deserializar2(path):
    Shelf = None
    try:
        Shelf = shelve.open(path,protocol=2)
        obj = Shelf['obj']
        L = Shelf['L']
        return obj, L

    except Exception as e:
        print("ERROR al deserializar", e)

    finally:
        if Shelf: Shelf.close

def crearDict():
    return {letra:[Punto2D(randint(-10,10),randint(-10,10)) for _ in range(5)] \
        for letra in string.ascii_uppercase}

def printDict(dicc):
    for letra, L in dicc.items():
        print(letra, L)

if __name__ == '__main__':
    d = crearDict()
    #printDict(d)
    L = list(range(20))

    serializar2("serializacion.bin", d, L)
    d2,L2 = deserializar2("serializacion.bin")
    print(d2)
    print(L2)

    """
    serializar("diccionario.bin", d)
    d2 = deserializar("diccionario.bin")
    printDict(d2)
    """