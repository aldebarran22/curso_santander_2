"""
POO en Python. sobrecarga de operadores aritmeticos
"""
from math import sqrt

class Punto2D:

    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Punto2D(self.x + other.x, self.y + other.y)

    def distancias(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def __repr__(self):
        return str(self)

class Nube:

    def __init__(self, p, *args):       
        self.puntos = [p]
        self.puntos.extend(args)
    
    def add(self, *args):
        self.puntos.extend(args)
    
    def masCercano(self, origen):
        """Calcular el punto mas cercano al origen
        """
        pass

if __name__ == '__main__':
    p = Punto2D(2,6)
    q = Punto2D(-3,7)
    r = p + q
    print(r)

    nube = Nube(p,q,r)    
    nube2 = Nube(Punto2D(0,0))

    print(nube.puntos)
    print(nube2.puntos)
