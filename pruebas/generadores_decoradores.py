# generadores:
L=[1,2,3,4,5]
l2=(n**2 for n in L)
print(l2)

for i in l2:
	print(i)
	
	
def imp(s):
	return s



def mi_decorador(funcion): 
	def nueva(*args): 
		print ("Llamada a la funcion", funcion.__name__ )
		retorno = funcion(*args) 
		return retorno 
	return nueva

mi_decorador(imp)("hola")
