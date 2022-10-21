
myGlobal = 5

def func1():
	global myGlobal
	myGlobal = 42

def func2():
    print (myGlobal)

func1()
func2()





# datos globales:
num = 234
L=[1,2,3]


def funcion():
	# Accede a las variables globales en modo lectura:
	# No hace global, ni se distingue entre mutable e inmutable
	print("num:",num)
	print("L:",L)
	
def funcion2():
	# Si la variable global es un tipo inmutable y la vamos a modificar
	# es necesario poner global:
	
	# Si el objeto es mutable y lo vamos a modificar MEDIANTE UNA ASIGNACION
	# en este si es obligatorio poner global
	global num,L
	num+=2
	L+=[45]
		
def funcion3():
	# Si el objeto es mutable y se modifica con un metodo NO ES NECESARIO
	# PONER global
	L.append(8)	
	
funcion()
funcion2()
funcion()
funcion3()
funcion()
