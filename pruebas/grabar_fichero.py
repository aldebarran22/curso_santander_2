lista=['sota','caballo','rey']

fichero=open('prueba.txt','w')
for x in lista:
	fichero.write(x+'\n')
fichero.close()

fichero=open('prueba.txt','r')
mi_cadena = fichero.read()
fichero.seek(0)
lista=fichero.readlines()
print(lista)

fichero.seek(0)
for linea in fichero.readlines():
	print(linea)
fichero.close()	
