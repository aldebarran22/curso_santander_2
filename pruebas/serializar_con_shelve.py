import shelve

animales = ["piton", "mono", "camello"]
lenguajes = ["python", "mono", "perl"]
shelf = shelve.open("datos.dat")
shelf["primera"] = animales
shelf["segunda"] = lenguajes
print (shelf["segunda"])
shelf.close()

s2 = shelve.open("datos.dat")
print('Despues de cerrar:', s2['primera'])
for k,v in s2.items():
	print(k,v)
	
s2.close()

