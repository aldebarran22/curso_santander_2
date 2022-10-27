"""
Lectura de un fichero
"""

import sys

def imprimirFichero(path):
    f = None
    try:
        f = open(path, 'r')
        for linea in f:
            print(linea.rstrip())

    except IOError as e:
        print(e)

    finally:
        if f: f.close()


if __name__ == '__main__':
    path = sys.argv[0]
    imprimirFichero(path)