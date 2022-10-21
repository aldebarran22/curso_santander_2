# Leer un fichero con un iterador:

print("Imprimir el contenido de un archivo")
with open("consola.py") as fp:
	for linea in iter(fp.readline,''):
		print(linea)


