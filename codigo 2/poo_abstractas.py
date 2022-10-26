"""
Ejemplo de una clase Abstracta
"""

from abc import ABC
import abc
from math import pi

class Figura(ABC):

    def __init__(self, color="red", etiqueta=""):
        self.color = color
        self.nombre = etiqueta

    @abc.abstractmethod
    def area(self):
        pass

    def __str__(self):
        return self.nombre+" "+self.color

class Circulo(Figura):

    def __init__(self,color="red", etiqueta="", radio=5.0):
        Figura.__init__(self,color,etiqueta)
        self.radio = radio

    def area(self):
        return pi * self.radio**2

    def __str__(self):
        return Figura.__str__(self) + " area: " + str(self.area())

if __name__ == '__main__':
    #f = Figura('green','figura1')        
    cir = Circulo('yellow','circulo1',3.0)
    print(cir)