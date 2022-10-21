"""Primer elemento de la función texto se toma como __doc__"""

def haz_algo(arg): 
	"""Este es el docstring de la funcion."""
	print (arg)

# Acceso a la doc en tiempo de ejecución:
print (haz_algo.__doc__)

# Cambio de la documentación:
haz_algo.__doc__ = """Este es un nuevo docstring."""
print (haz_algo.__doc__)
print(__doc__)
