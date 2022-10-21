# objetos:

class Pair:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Pair({0.x!r}, {0.y!r})'.format(self)
	
	def __str__(self):
		return '({0.x!s}, {0.y!s})'.format(self)
		
		
p=Pair(2,4)
print(type(p))	
print(repr(p))
print(p)	


class Coche: 
	"""Abstraccion de los objetos coche."""

	def __init__(self, gasolina): 
		self.gasolina = gasolina 
		print ("Tenemos", gasolina, "litros")

	def arrancar(self): 
		if self.gasolina > 0: 
			print("Arranca")
		else: 
			print("No arranca")

	def conducir(self): 
		if self.gasolina > 0: 
			self.gasolina -= 1 
			print("Quedan", self.gasolina, "litros")
		else: 
			print("No se mueve")

miCoche = Coche(3)
miCoche.arrancar()
print(miCoche.gasolina)
print(type(miCoche))

class Perro:

    tipo = 'canino'                 # variable de clase compartida por todas las instancias

    def __init__(self, nombre):
        self.nombre = nombre        # variable de instancia única para la instancia

 
d = Perro('Fido')
e = Perro('Buddy')
print(d.tipo)                    # compartido por todos los perros
print(e.tipo)                    # compartido por todos los perros
print(d.nombre)                  # único para d
print(e.nombre)                  # único para e


class Perro2:

	tipo = 'canino'                
	
	def __init__(self, nombre):
		self.nombre = nombre        
		self.trucos=[]
        
	def agregar_truco(self, truco):
		self.trucos.append(truco)

 
d = Perro2('Fido')
e = Perro2('Buddy')
d.agregar_truco('girar')
e.agregar_truco('hacerse el muerto')
print(d.tipo)                    # compartido por todos los perros
print(e.tipo)                    # compartido por todos los perros
print(d.nombre)                  # único para d
print(e.nombre)                  # único para e

print(d.trucos)
print(e.trucos)

class Persona(object):
	"""Doc  de la clase Persona"""	
	
	def __init__(self, nombre):
		self.nombre = nombre
	
	def __str__(self):
		return self.nombre	
	
class Empleado(Persona):
	
	def __init__(self, nombre, sueldo):				
		#Persona.__init__(self, nombre)		
		super().__init__(nombre)
		self.sueldo = sueldo
		
	def __str__(self):
		#return Persona.__str__(self) + " " + str(self.sueldo)
		return super().__str__() + " " + str(self.sueldo)
	
print("\n\nPRUEBAS CON LA HERENCIA")	
p = Persona("Pedro")
e = Empleado("Ana", 2000)
print("empleado: ", e)

if isinstance(e, Persona):
	print("Si es una instancia")

if issubclass(Empleado,Persona):
	print("Si es una subclase")
	
print(p.__class__)
print("Nombre de la clase:", e.__class__.__name__)
print(Persona.__subclasses__())	
#print(help(Persona))

if hasattr(p, "nombre"):
	print("si lo tiene")
	
	
print(getattr(p,"nombre"))		

