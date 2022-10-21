#prueba clase padre:

class ClaseA():
	
	accesos=[]
	
	def __init__(self, a):
		self.a=a
		ClaseA.accesos.append(a)
		
	def __str__(self):
		return str(self.a)	
		
	@staticmethod
	def listar_accesos():
		ClaseA.accesos.sort()
		for a in ClaseA.accesos:
			print("Acceso:",a)
		
	
uno=ClaseA(1)
dos=ClaseA(2)
ClaseA.listar_accesos()	
	
	
class ClaseB():
	
	def __new__(cls, *args, **kwargs):
		print('pasa por new')	
		new_instance = object.__new__(cls)
		return new_instance
		
		
	def __init__(self,b):
		self.b = b
		print('pasa por init')
		
	def __str__(self):
		return  str(self.b)
	
	
b = ClaseB(5)	
print(b)	
print(b.__class__)
print(b.__class__.__class__)	
