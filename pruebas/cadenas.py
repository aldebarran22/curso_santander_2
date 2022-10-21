# cadenas de texto:
s = 'hola\tadios\tmas'
r = "hola\tadios\tmas"

print("s:",s)
print("r:",r)

print("tipo",type(s))

s = r"cadena raw"
print(type(s))

triple = """ hola que tal
esta es una cadena triple"""

print(triple)

print(triple*3)

if 'ola' in r:
	print("encontrado")
else:
	print("No encontrado")

