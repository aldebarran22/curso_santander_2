class Prueba():
	
	def __init__(self, a):
		self.__a = a
		
		
	def __str__(self):
		return str(self.__a)
		
	def __privado(self):
		return 10*str(self.__a)
		
	def __otro__(self):
		return 20*str(self.__a)	
		
print(dir(Prueba))
print()
p=Prueba(8)
print(p.__dict__)
print()
print("dir:",p.__dir__())
print()
print("sizeof:",p.__sizeof__())
print()
print("otro:",p.__otro__())
print()
print(p.__privado())
		
