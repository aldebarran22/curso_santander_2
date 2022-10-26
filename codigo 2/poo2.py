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

    def dist(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def __repr__(self):
        return str(self)

class Nube:

    def __init__(self, p, *args):       
        self.puntos = [p]
        self.puntos.extend(args)
        self.indice = 0
    
    def add(self, *args):
        self.puntos.extend(args)
    
    def masCercano(self, origen):
        """Calcular el punto mas cercano al origen
        """
        distancias = [origen.dist(p) for p in self.puntos]        
        dMasCercana = min(distancias)        
        pos = distancias.index(dMasCercana)       
        return self.puntos[pos]

    def __len__(self):
        return len(self.puntos)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == len(self.puntos):
            self.indice = 0
            raise StopIteration
        else:
            val = self.puntos[self.indice]
            self.indice+=1
            return val

if __name__ == '__main__':
    p = Punto2D(2,6)
    q = Punto2D(-3,7)
    r = p + q
    print(r)
    print('x:', getattr(p, "x"))
    setattr(p, "x",100)
    print(p)

    nube = Nube(p,q,r)    
    print(nube.puntos)
    print(nube.masCercano(Punto2D(0,0)))
    print('La nube tiene',len(nube),'puntos')
    for p in nube:
        print(p)

    print('Segunda vez')
    for p in nube:
        print(p)

    