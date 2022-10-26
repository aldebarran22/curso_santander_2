"""
Ejemplo de POO en Python
"""

class Persona:
    """
    implementación de la clase Persona
    """
    # At. de clase
    num_instancias = 0
    
    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        Persona.num_instancias += 1

    @staticmethod
    def getNumInstancias():
        return Persona.num_instancias

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __lt__(self, other):        
        return self.edad < other.edad

    def __eq__(self, other):        
        return self.nombre == other.nombre \
            and self.edad == other.edad \
                and self.altura == other.altura

    def __repr__(self):
        return str(self)

    def cumple(self):
        self.edad+=1

    def hablar(self, other=None):
        if not other:
            print(self.nombre,"esta hablando solo")
        else:
            print(self.nombre,'habla con',other.nombre)

    def __del__(self):
        Persona.num_instancias -= 1
        #print('Eliminando a', self.nombre)

if __name__ == '__main__':
    print(Persona.getNumInstancias(),'instancias')
    p1 = Persona("Juan",34,altura=1.77)
    p2 = Persona("Ana",34,altura=1.77)
    if p1 == p2:
        print('iguales')
    else:
        print('distintos')

    p1.hablar()
    p1.hablar(p2)
    print(p1.__dict__)
    p3 = Persona("Gema")
    print(Persona.getNumInstancias(),'instancias')
    del(p3)
    print(Persona.getNumInstancias(),'instancias')    

    if p1 < p2:  # p1.__lt__(p2)
        print(p1.nombre,"es menor que",p2.nombre)

    print(p1) # print(str(p1))  print(p1.__str__())
    L = [p1, p2, Persona('Alberto',33,1.8)]
    print(L)
    L.sort()
    print(L)
    L.sort(key=lambda obj : obj.altura, reverse=True)    
    print(L)
    L[0].tno = 600695926
    L[0].__dict__['apellido']="Sanz"
    L2 = [obj.__dict__ for obj in L]
    print(L2)
    print(L[0].tno, L[0].apellido)

    print(p1)
    f = p1.cumple
    f()
    print(p1)
    Persona.cumple(p1)
    print(p1)



